import { Map, View } from "ol";
import { defaults as defaultControls } from 'ol/control/defaults.js';
import GeoJSON from "ol/format/GeoJSON";
import Overlay from "ol/Overlay";
import { fromLonLat, transformExtent, useGeographic } from "ol/proj";
import { JSONConverter } from "./json";
import { addTooltipToMap } from "./tooltip";
import { addSelectFeaturesToMap } from "./select-features";

// --- Types
import type Layer from "ol/layer/Layer";
import type Control from "ol/control/Control";
import type VectorSource from "ol/source/Vector";
import type VectorLayer from "ol/layer/Vector";
import type WebGLVectorLayer from "ol/layer/WebGLVector";
import type { Coordinate } from "ol/coordinate";
import type { MyMapOptions } from ".";

import type { AnyModel } from "@anywidget/types";

type Metadata = {
  layers: any[];
  controls: any[];
};

// --- Constants
// TODO: Move to constants
const TYPE_IDENTIFIER = "@@type";
const GEOJSON_IDENTIFIER = "@@geojson";

const jsonConverter = new JSONConverter();

// ...
useGeographic();

// --- Helpers
function parseViewDef(viewDef: JSONDef): View {
  const view = jsonConverter.parse(viewDef) as View;
  const center = view.getCenter();
  console.log("view center", center);
  // Not needed anymore because of `useGeographic()`
  /*
  if (center && view.getProjection().getCode() !== "EPSG:4326") {
    const centerTransformed = fromLonLat(center);
    console.log("view center transformed", centerTransformed);
    view.setCenter(centerTransformed);
  }*/

  return view;
}

function parseLayerDef(layerDef: JSONDef): Layer {
  const layer = jsonConverter.parse(layerDef);
  console.log("layerDef", layerDef);
  layer.set("id", layerDef.id);
  addGeojsonFeatures(layer, layerDef["source"][GEOJSON_IDENTIFIER]);
  return layer;
}

function addGeojsonFeatures(layer: Layer, features: any): void {
  if (features) {
    const source = layer.getSource() as VectorSource;
    source.addFeatures(new GeoJSON().readFeatures(features));
    console.log("geojson features added", features);
  }
}

// --- Base class
export default class MapWidget {
  _container: HTMLElement;
  _map: Map;
  _metadata: Metadata = { layers: [], controls: [] };
  _model: AnyModel | undefined;

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions, model?: AnyModel | undefined) {
    this._model = model;

    const view = parseViewDef(mapOptions.view);
    let baseControls: Control[] = [];
    let baseLayers: Layer[] = [];

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

  getElement(): HTMLElement {
    return this._container;
  }

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

  setExtentFromSource(layerId: string): void {
    const source = this.getLayer(layerId)?.getSource() as VectorSource;
    if (source) {
      // TODO: Only works if event is not already fired
      source.on("featuresloadend", (e) => {
        const extent = source.getExtent();
        console.log("extent", layerId, extent);
        this.fitBounds(extent);
      })
    }
  }

  fitBounds(extent: any): void {
    this._map.getView().fit(extent);
  }

  // TODO: obsolete since `useGeographic()` does this for us
  fitBoundsFromLonLat(extentLonLat: any): void {
    const exent = transformExtent(extentLonLat, "EPSG:4326", this._map.getView().getProjection());
    this.fitBounds(exent);
  }

  setView(viewDef: JSONDef): void {
    const view = jsonConverter.parse(viewDef) as View;
    this._map.setView(view);
  }

  // --- View Methods
  applyCallToView(call: OLAnyWidgetCall): void {
    const view = this._map.getView();
    console.log("run view method", view);

    // @ts-expect-error
    view[call.method](...call.args)
  }

  // --- Layer methods
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

  // --- Control methods
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

  // ...
  addOverlay(position: Coordinate | undefined, html: string, cssText: string | undefined, id: string = "ol-overlay"): void {
    const el = document.createElement("div");
    el.id = id;
    el.style.cssText = cssText || "";
    el.innerHTML = html;
    const overlay = new Overlay({ element: el, position: position });
    this._map.addOverlay(overlay);
  }

  // ...
  addTooltip(template: string | null): void {
    addTooltipToMap(this._map, template);
  }

  addSelectFeatures(): void {
    addSelectFeaturesToMap(this._map);
  }
}
