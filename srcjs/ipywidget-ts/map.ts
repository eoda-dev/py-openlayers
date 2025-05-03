import { Map, View } from "ol";
// import type { ViewOptions } from "ol/View";

// import TileLayer from "ol/layer/Tile";

// import OSM from "ol/source/OSM";

import { defaults as defaultControls } from 'ol/control/defaults.js';
// import { MapOptions } from "ol/Map";

import GeoJSON from "ol/format/GeoJSON";

import Overlay from "ol/Overlay";

import { JSONConverter } from "./json";

// import { addTooltipTo } from "./tooltip"; // Uses an overlay
import { addTooltip2 } from "./tooltip2"; // Uses custom div container

// import { populatedPlacesLayer } from "./test-json-converter";
import type Layer from "ol/layer/Layer";
import type Control from "ol/control/Control";

import type VectorSource from "ol/source/Vector";

import type VectorLayer from "ol/layer/Vector";
import type WebGLVectorLayer from "ol/layer/WebGLVector";

import { transform as transformProj, fromLonLat } from "ol/proj";

// My types
import type { MyMapOptions } from ".";
import type { Coordinate } from "ol/coordinate";

// ...
/*
type LayerStore = {
  [key: string]: Layer;
};
*/

//
/* 
type ControlStore = {
  [key: string]: Control;
};
*/

//
type Metadata = {
  layers: any[];
  controls: any[];
};

const TYPE_IDENTIFIER = "@@type";
const GEOJSON_IDENTIFIER = "@@geojson";

const jsonConverter = new JSONConverter();

function parseViewDef(viewDef: JSONDef): View {
  const view = jsonConverter.parse(viewDef) as View;
  const center = view.getCenter();
  console.log("view center", center)
  if (center && view.getProjection().getCode() !== "EPSG:4326") {
    const centerTransformed = fromLonLat(center);
    console.log("view center transformed", centerTransformed);
    view.setCenter(centerTransformed);
  }

  return view;
}

function parseLayerDef(layerDef: JSONDef): Layer {
  const layer = jsonConverter.parse(layerDef);
  layer.set("id", layerDef.id);
  addGeojsonFeatures(layer, layerDef[GEOJSON_IDENTIFIER]);
  return layer;
}

function addGeojsonFeatures(layer: Layer, features: any): void {
  if (features === undefined)
    return;

  const source = layer.getSource() as VectorSource;
  source.addFeatures(new GeoJSON().readFeatures(features));
  console.log("geojson features added", features);
}


export default class MapWidget {
  _container: HTMLElement;
  _map: Map;
  _metadata: Metadata = { layers: [], controls: [] };

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions) {
    let baseLayers: Layer[] = [] // defaultLayers;
    /*
    if (mapOptions.layers !== undefined) {
      for (let layerJSONDef of mapOptions.layers) {

        // TODO: Duplicated code, use 'addLayer' after map was created instead
        const layer = jsonConverter.parse(layerJSONDef);

        // if (layerJSONDef.source["@@geojson"] !== undefined)
        this.addGeoJSONToSource(layer, layerJSONDef.source["@@geojson"]);

        baseLayers.push(layer);
        this._layerStore[layerJSONDef.id] = layer;
      }
    }
    */

    let baseControls: Control[] = [];
    // TODO: Use 'addControls' after map was created instead
    /*
    if (mapOptions.controls !== undefined) {
      for (let controlJSONDef of mapOptions.controls) {
        const control = jsonConverter.parse(controlJSONDef);
        baseControls.push(control);
        this._controlStore[controlJSONDef.id] = control;
      }
    }
    */

    // TODO: Move to func 'parseView'
    /*
    const view = jsonConverter.parse(mapOptions.view) as View;
    const center = view.getCenter();
    console.log("center", center)
    if (center && view.getProjection().getCode() !== "EPSG:4326") {
      const centerTransformed = fromLonLat(center);
      console.log("centerTransformed", centerTransformed);
      view.setCenter(centerTransformed);
    }
      */
    const view = parseViewDef(mapOptions.view);

    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: view,
      controls: defaultControls().extend(baseControls),
      layers: baseLayers,
    });

    // Add controls
    for (let controlDef of mapOptions.controls || []) {
      this.addControl(controlDef);
    }

    // Add layers
    for (let layerDef of mapOptions.layers || []) {
      this.addLayer(layerDef);
    }
  }

  // TODO: Obsolete
  /*
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
  */

  getMap(): Map {
    return this._map;
  }

  getMetadata(): Metadata {
    return this._metadata;
  }

  setViewFromSource(layerId: string): void {
    const layer = this.getLayer(layerId);
    const source = layer?.getSource();
    const view = source?.getView();
    if (view)
      this._map.setView(view);
  }

  setExtentFromSource(): void {

  }

  /*
  addGeoJSONToSource(layer: Layer, geoJSONObject: any): void {
    if (geoJSONObject === undefined)
      return;

    const source = layer.getSource() as VectorSource;
    source.addFeatures(new GeoJSON().readFeatures(geoJSONObject));
    console.log("geojsonObject added to VectorSource", geoJSONObject);
  }
  */

  /*
  addLayerOld(layerJSONDef: JSONDef): void {
    const layer = jsonConverter.parse(layerJSONDef);
    layer.set("id", layerJSONDef.id);

    //if (layerJSONDef.source["@@geojson"] !== undefined)
    this.addGeoJSONToSource(layer, layerJSONDef.source["@@geojson"]);

    this._map.addLayer(layer);
    this._layerStore[layerJSONDef.id] = layer;
    console.log("layerStore", this._layerStore);
  }
  */

  // --- Layers
  getLayer(layerId: string): Layer | undefined {
    for (let layer of this._map.getLayers().getArray()) {
      if (layer.get("id") === layerId)
        return layer as Layer;
    }
  }

  addLayer(layerDef: JSONDef): void {
    const layer = parseLayerDef(layerDef);
    this._map.addLayer(layer);
    this._metadata.layers.push({
      id: layer.get("id"),
      type: layerDef[TYPE_IDENTIFIER]
    });
    console.log("layer", layer.get("id"), "added", this._metadata);
  }

  removeLayer(layerId: string): void {
    const layer = this.getLayer(layerId);
    if (layer) {
      this._map.removeLayer(layer);
      this._metadata.layers = this._metadata.layers.filter(item => item["id"] != layerId);
      console.log("layer", layerId, "removed", this._metadata);
    }
  }

  // --- Controls
  getControl(controlId: string): Control | undefined {
    for (let control of this._map.getControls().getArray()) {
      if (control.get("id") === controlId)
        return control;
    }
  }

  addControl(controlDef: JSONDef): void {
    const control = jsonConverter.parse(controlDef);
    control.set("id", controlDef.id);
    this._map.addControl(control);
    this._metadata.controls.push({
      id: control.get("id"),
      type: controlDef[TYPE_IDENTIFIER],
    });
    console.log("control", control.get("id"), "added", this._metadata);
  }

  removeControl(controlId: string): void {
    const control = this.getControl(controlId);
    if (control) {
      this._map.removeControl(control);
      this._metadata.controls = this._metadata.controls.filter(item => item["id"] != controlId);
      console.log("control", controlId, "removed", this._metadata);
    }
  }

  // --- Misc
  setLayerStyle(layerId: string, style: any): void {
    const layer = this.getLayer(layerId) as VectorLayer | WebGLVectorLayer;
    if (layer) {
      console.log("set layer style", layerId, style);
      layer.setStyle(style)
    }
  }

  applyCallToLayer(layerId: string, call: OLAnyWidgetCall): void {
    console.log("run layer method", layerId);
    const layer = this.getLayer(layerId);

    // @ts-expect-error
    layer[call.method](...call.args)
  }

  // TODO: Remove
  testJSONDef(jsonDef: JSONDef): any {
    return jsonConverter.parse(jsonDef);
  }

  // TODO: Remove
  debugData(data: any): void {
  }

  // TODO: Test only at the moment
  addOverlay(position: Coordinate | undefined): void {
    const el = document.createElement("div");
    el.style.cssText = "";
    el.innerHTML = "We are out here."
    const overlay = new Overlay({ element: el, position: position });
    this._map.addOverlay(overlay);
  }

  // ...
  addTooltip(prop: string | null): void {
    addTooltip2(this._map, prop);
  }
}
