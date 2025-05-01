import { Feature, Map, View } from "ol";
import { type ViewOptions } from "ol/View";

import TileLayer from "ol/layer/Tile";

import OSM from "ol/source/OSM";

import { defaults as defaultControls } from 'ol/control/defaults.js';
// import { MapOptions } from "ol/Map";

import GeoJSON from "ol/format/GeoJSON";

import Overlay from "ol/Overlay";

import { JSONConverter } from "./json";

import { addTooltipTo } from "./tooltip";

// import { populatedPlacesLayer } from "./test-json-converter";
import type Layer from "ol/layer/Layer";
import type Control from "ol/control/Control";

import type VectorSource from "ol/source/Vector";

import type VectorLayer from "ol/layer/Vector";
import type WebGLVectorLayer from "ol/layer/WebGLVector";

import { transform as transformProj, fromLonLat } from "ol/proj";

// My types
import { type MyMapOptions } from ".";
import { type Coordinate } from "ol/coordinate";

// ...
type LayerStore = {
  [key: string]: Layer;
}

// 
type ControlStore = {
  [key: string]: Control;
}

const jsonConverter = new JSONConverter();

/*
const defaultLayers = [
  new TileLayer({
    source: new OSM()
  })
];
*/

export default class MapWidget {
  _container: HTMLElement;
  _map: Map;
  _layerStore: LayerStore = {};
  _controlStore: ControlStore = {};

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions) {
    let baseLayers: Layer[] = [] // defaultLayers;
    if (mapOptions.layers !== undefined) {
      for (let layerJSONDef of mapOptions.layers) {

        // TODO: Duplicated code, use 'addLayer' after map was created instead
        const layer = jsonConverter.parse(layerJSONDef);

        if (layerJSONDef.source["@@geojson"] !== undefined)
          this.addGeoJSONToSource(layer, layerJSONDef.source["@@geojson"]);

        baseLayers.push(layer);
        this._layerStore[layerJSONDef.id] = layer;
      }
    }


    let baseControls: Control[] = [];
    // TODO: Use 'addControls' after map was created instead
    if (mapOptions.controls !== undefined) {
      for (let controlJSONDef of mapOptions.controls) {
        const control = jsonConverter.parse(controlJSONDef);
        baseControls.push(control);
        this._controlStore[controlJSONDef.id] = control;
      }
    }

    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      // view: new View(mapOptions.viewOptions),
      view: new View(this.transformCenter(mapOptions.viewOptions)),
      controls: defaultControls().extend(baseControls),
      layers: baseLayers,
    });
  }


  transformCenter(viewOptions: ViewOptions): ViewOptions {
    const center = viewOptions.center;
    if (center && viewOptions.projection !== "EPSG:4326") {
      // console.log("center before", center);
      viewOptions.center = fromLonLat(center);
      // viewOptions.center = transformProj(center, "EPSG:4326", viewOptions.projection || "EPSG:3857");
      // console.log("center after", viewOptions.center);
    }
    return viewOptions;
  }


  getMap(): Map {
    return this._map;
  }

  getLayerOld(layerId: string): Layer {
    return this._layerStore[layerId];
  }

  getLayer(layerId: string): Layer | undefined {
    for (let layer of this._map.getLayers().getArray()) {
      if (layer.get("id") === layerId)
        return layer as Layer;
    }
  }

  getControl(controlId: string): Control {
    return this._controlStore[controlId];
  }

  setViewFromSource(layerId: string): void {
    const layer = this.getLayer(layerId); // this._layerStore[layerId];
    const source = layer?.getSource();
    const view = source?.getView();
    if (view !== undefined) this._map.setView(view);
  }

  setExtentFromSource(): void {

  }

  addGeoJSONToSource(layer: Layer, geoJSONObject: any): void {
    const source = layer.getSource() as VectorSource;
    // const options = { dataProjection: "EPSG:4326", featureProjection: "EPSG:4326" };

    source.addFeatures(new GeoJSON().readFeatures(geoJSONObject));
    console.log("geojsonObject added to VectorSource", geoJSONObject);
  }

  addLayer(layerJSONDef: JSONDef): void {
    const layer = jsonConverter.parse(layerJSONDef);

    if (layerJSONDef.source["@@geojson"] !== undefined)
      this.addGeoJSONToSource(layer, layerJSONDef.source["@@geojson"]);

    this._map.addLayer(layer);
    this._layerStore[layerJSONDef.id] = layer;
    console.log("layerStore", this._layerStore);
  }

  removeLayer(layerId: string): void {
    const layer = this.getLayer(layerId); // this._layerStore[layerId];
    if (layer === undefined) return;

    this._map.removeLayer(layer);
    delete this._layerStore[layerId];
    console.log("layer", layerId, "removed", this._layerStore);
  }

  addControl(controlJSONDef: JSONDef): void {
    const control = jsonConverter.parse(controlJSONDef);
    this._map.addControl(control);
    this._controlStore[controlJSONDef.id] = control;
    console.log("controlStore", this._controlStore);
  }

  removeControl(controlId: string): void {
    const control = this._controlStore[controlId];
    if (control === undefined) return;

    this._map.removeControl(control);
    delete this._controlStore[controlId];
    console.log("control", controlId, "removed", this._controlStore);
  }

  /*
  setLayerProperty(layerId: string, prop: string, value: any): void {
    const layer = this.getLayer(layerId);
    layer.set(prop, value);
  }
  */

  setLayerStyle(layerId: string, style: any): void {
    const layer = this.getLayer(layerId) as VectorLayer | WebGLVectorLayer;
    layer.setStyle(style)
  }

  applyCallToLayer(layerId: string, call: OLAnyWidgetCall): void {
    console.log("layer call", "layerId", layerId);
    const layer = this.getLayer(layerId);

    // @ts-expect-error
    layer[call.method](...call.args)
  }

  testJSONDef(jsonDef: JSONDef): any {
    return jsonConverter.parse(jsonDef);
  }

  // ...
  debugData(data: any): void {
  }

  // ...
  addOverlay(position: Coordinate | undefined): void {
    const el = document.createElement("div");
    el.style.cssText = "";
    el.innerHTML = "We are out here."
    const overlay = new Overlay({ element: el, position: position });
    this._map.addOverlay(overlay);
  }

  // ...
  addTooltip(prop: string): void {
    addTooltipTo(this._map, prop);
  }
}
