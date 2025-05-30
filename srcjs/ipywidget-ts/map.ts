import { Map, View } from "ol";
// import { defaults as defaultControls } from 'ol/control/defaults.js';
import GeoJSON from "ol/format/GeoJSON";
import Overlay from "ol/Overlay";
import { useGeographic } from "ol/proj";
import { isEmpty } from "ol/extent";
import Modify from "ol/interaction/Modify";
import Snap from "ol/interaction/Snap";

import { JSONConverter } from "./json";
import { TYPE_IDENTIFIER, GEOJSON_IDENTIFIER } from "./constants";
import { defaultControls } from "./controls";
import { parseClickEvent } from "./utils";
// import { DrawControl } from "./custom-controls/draw";

import { featureToGeoJSON } from "./utils";
import { addTooltipToMap } from "./tooltip";
import { addEventListernersToMapWidget } from "./events";
import { addSelectFeaturesToMap } from "./select-features";
import { addDragAndDropToMap as addDragAndDropVectorLayersToMap } from "./drag-and-drop";

// --- Types
import type Layer from "ol/layer/Layer";
import type Control from "ol/control/Control";
import type VectorSource from "ol/source/Vector";
import type VectorLayer from "ol/layer/Vector";
import type WebGLVectorLayer from "ol/layer/WebGLVector";
import type { Coordinate } from "ol/coordinate";
import type { FlatStyle } from "ol/style/flat";
import type { MyMapOptions } from ".";

import type { AnyModel } from "@anywidget/types";

type Metadata = {
  layers: any[];
  controls: any[];
};

// TODO: Rename to something like `FeatureStore`
type Features = {
  [layerId: string]: any[];
}

const jsonConverter = new JSONConverter();

// --- Use geographic coordinates (WGS-84) in all methods
useGeographic();

function parseLayerDef(layerDef: JSONDef): Layer {
  const layer = jsonConverter.parse(layerDef);
  console.log("layerDef", layerDef);
  layer.setProperties({
    id: layerDef.id,
    type: layerDef[TYPE_IDENTIFIER]
  });
  addGeojsonFeatures(layer, layerDef.source[GEOJSON_IDENTIFIER]);
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
  // _features: Features = {};
  _model: AnyModel | undefined;

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions, model?: AnyModel | undefined) {
    this._model = model;

    const view = jsonConverter.parse(mapOptions.view) as View;

    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: view,
      controls: [],
      layers: []
    });

    // Add event listeners
    addEventListernersToMapWidget(this);

    // Add default controls
    for (const defaultControl of defaultControls)
      this._map.addControl(defaultControl);


    // Add controls
    for (let controlDef of mapOptions.controls || []) {
      this.addControl(controlDef);
    }

    // Add layers
    for (let layerDef of mapOptions.layers || []) {
      this.addLayer(layerDef);
    }
  }

  // --- Functions
  getElement(): HTMLElement {
    return this._container;
  }

  getMap(): Map {
    return this._map;
  }

  getMetadata(): Metadata {
    return this._metadata;
  }

  getAnywidgetModel(): AnyModel | undefined {
    return this._model;
  }

  setViewFromSource(layerId: string): void {
    const view = this.getLayer(layerId)?.getSource()?.getView();
    if (view)
      this._map.setView(view);
  }

  setExtendByLayerId(layerId: string): void {
    const source = this.getLayer(layerId)?.getSource() as VectorSource;
    this.setExtentFromSource(source)
  }

  setExtentFromSource(source?: VectorSource): void {
    if (source) {
      if (isEmpty(source.getExtent())) {
        source.on("featuresloadend", (e) => {
          this._map.getView().fit(source.getExtent());
        });
      }
      else {
        this._map.getView().fit(source.getExtent());
      }
    }
  }

  fitBounds(extent: any): void {
    this._map.getView().fit(extent);
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

    // Fit bounds for VectorSources
    if (layer.get("fitBounds")) {
      const source = layer.getSource() as VectorSource;
      this.setExtentFromSource(source);
    }

    this._map.addLayer(layer);
  }

  removeLayer(layerId: string): void {
    const layer = this.getLayer(layerId);
    if (layer) {
      this._map.removeLayer(layer);
    }
  }

  setLayerStyle(layerId: string, style: any): void {
    const layer = this.getLayer(layerId) as VectorLayer | WebGLVectorLayer;
    if (layer) {
      layer.setStyle(style);
      console.log("style", layerId, "updated", style);
    }
  }

  applyCallToLayer(layerId: string, call: OLAnyWidgetCall): void {
    console.log("run layer method", layerId);
    const layer = this.getLayer(layerId);

    // @ts-expect-error
    layer[call.method](...call.args)
  }

  setSource(layerId: string, sourceDef: JSONDef): void {
    const layer = this.getLayer(layerId);
    if (layer) {
      const source = jsonConverter.parse(sourceDef);
      layer.setSource(source);
      const features = sourceDef[GEOJSON_IDENTIFIER];
      if (features)
        source.addFeatures(new GeoJSON().readFeatures(features));
    }
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
    control.setProperties({ id: controlDef.id, type: controlDef[TYPE_IDENTIFIER] });
    this._map.addControl(control);
  }

  removeControl(controlId: string): void {
    const control = this.getControl(controlId);
    if (control) {
      this._map.removeControl(control);
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
    addSelectFeaturesToMap(this._map, this._model);
  }

  addClickInteraction(): void {
    const model = this._model;
    this._map.on("click", (e) => {
      const info = parseClickEvent(e);
      console.log(info);
      if (model) {
        model.set("clicked", info);
        model.save_changes();
      }
    });
  }

  addDragAndDropVectorLayers(formatsDef?: JSONDef[], style?: FlatStyle): void {
    const formats = formatsDef?.map(item => jsonConverter.parse(item));
    console.log("drag and drop formats", formats);
    addDragAndDropVectorLayersToMap(this._map, formats, style);
  }

  // Does not work for `WebGLVectorLayer`
  addModifyInteraction(layerId: string): void {
    const source = this.getLayer(layerId)?.getSource() as VectorSource;
    if (source) {
      const snap = new Snap({ source: source });
      this._map.addInteraction(snap);
      const modify = new Modify({ source: source });
      this._map.addInteraction(modify);

      // Add event listener
      source.on("changefeature", (e) => {
        if (e.feature) {
          const feature = featureToGeoJSON(e.feature);
          console.log("feature changed", feature);
          if (this._model) {
            // this._features[layerId] = [feature];
            // this._model.set("features", this._features);
            this._model.set("features", { [layerId]: [feature] });
            this._model.save_changes();
          }
        }
      });
    }
  }
}
