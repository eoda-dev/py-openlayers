import { Map, View } from "ol";
// import { defaults as defaultControls } from 'ol/control/defaults.js';
import GeoJSON from "ol/format/GeoJSON";
import Overlay from "ol/Overlay";
import Draw from 'ol/interaction/Draw.js';
import { transformExtent, useGeographic } from "ol/proj";
// import { State as SourceState } from "ol/source/Source";
import { isEmpty } from "ol/extent";
import { JSONConverter } from "./json";
import { TYPE_IDENTIFIER, GEOJSON_IDENTIFIER } from "./constants";
import { defaultControls } from "./controls";

import { DrawControl } from "./draw-control";

import { addTooltipToMap } from "./tooltip";
import { addEventListernersToMapWidget } from "./events";
import { addSelectFeaturesToMap } from "./select-features";
import { addDragAndDropToMap as addDragAndDropVectorLayersToMap } from "./drag-and-drop";
import { drawSource, drawVectorLayer } from "./layers";

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
import type { Type as GeomType } from "ol/geom/Geometry";

type Metadata = {
  layers: any[];
  controls: any[];
};

// --- Constants
// TODO: Move to constants
// const TYPE_IDENTIFIER = "@@type";
// const GEOJSON_IDENTIFIER = "@@geojson";

const jsonConverter = new JSONConverter();

// --- Use geographic coordinates (WGS-84) in all methods
useGeographic();

function parseLayerDef(layerDef: JSONDef): Layer {
  const layer = jsonConverter.parse(layerDef);
  console.log("layerDef", layerDef);
  // Use setProperties instead
  layer.setProperties({
    id: layerDef.id,
    type: layerDef[TYPE_IDENTIFIER]
  });
  // layer.set("id", layerDef.id);
  // layer.set("type", layerDef[TYPE_IDENTIFIER]);

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
  _draw: Draw | undefined;
  _model: AnyModel | undefined;

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions, model?: AnyModel | undefined) {
    this._model = model;

    const view = jsonConverter.parse(mapOptions.view) as View;
    // let baseControls: Control[] = [];
    // let baseLayers: Layer[] = [];

    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: view,
      controls: [], // defaultControls,
      layers: [] // baseLayers,
    });

    // events
    addEventListernersToMapWidget(this);

    this._map.addControl(new DrawControl({}));

    for (const defaultControl of defaultControls)
      this._map.addControl(defaultControl);
    /*
    this._map.getLayers().on("add", (e) => {
      const layer = e.element;
      console.log("layer add", layer.getProperties());
    });
    */

    /*
    this._map.on("loadend", () => this.updateMetadata());

    this._map.getControls().on("propertychange", (e) => {
      this.updateMetadata();
      console.log("control added or removed", this._metadata);
    });

    this._map.getLayers().on("propertychange", (e) => {
      this.updateMetadata();
      console.log("layer added or removed", this._metadata);
    });
    */
    // ---

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

  getAnywidgetModel(): AnyModel | undefined {
    return this._model;
  }

  /*
  updateMetadata(): void {
    const layers = this._map.getLayers().getArray().map(l => ({
      id: l.get("id"),
      type: l.get("type"),
      // extent: l.getExtent()
      // properties: l.getProperties()
    }));
    this._metadata.layers = layers;
    const controls = this._map.getControls().getArray().map(c => ({
      id: c.get("id"),
      type: c.get("type"),
      // properties: c.getProperties()
    }));
    this._metadata.controls = controls;
    if (this._model) {
      this._model.set("metadata", this._metadata);
      this._model.save_changes();
      console.log("model data updated", this._metadata, this._map.getLayers().getArray());
    }
  }
  */

  setViewFromSource(layerId: string): void {
    const view = this.getLayer(layerId)?.getSource()?.getView();
    // const source = layer?.getSource();
    // const view = source?.getView();
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

  // TODO: obsolete since `useGeographic()` does this for us
  /*
  fitBoundsFromLonLat(extentLonLat: any): void {
    const exent = transformExtent(extentLonLat, "EPSG:4326", this._map.getView().getProjection());
    this.fitBounds(exent);
  }
  */

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
      /*
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
      */
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
    // control.set("id", controlDef.id);
    // control.set("type", controlDef[TYPE_IDENTIFIER])
    control.setProperties({ id: controlDef.id, type: controlDef[TYPE_IDENTIFIER] });
    this._map.addControl(control);
    /*
    this._metadata.controls.push({
      id: control.get("id"),
      type: controlDef[TYPE_IDENTIFIER],
    });
    */
    // console.log("control", control.get("id"), "added", this._metadata);
  }

  removeControl(controlId: string): void {
    const control = this.getControl(controlId);
    if (control) {
      this._map.removeControl(control);
      // this._metadata.controls = this._metadata.controls.filter(item => item["id"] != controlId);
      // console.log("control", controlId, "removed", this._metadata);
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

  addDragAndDropVectorLayers(formatsDef?: JSONDef[], style?: FlatStyle): void {
    const formats = formatsDef?.map(item => jsonConverter.parse(item));
    console.log("drag and drop formats", formats);
    addDragAndDropVectorLayersToMap(this._map, formats, style);
  }

  // See https://openlayers.org/en/latest/examples/draw-and-modify-features.html
  addDrawInteraction(type: GeomType): void {
    if (this._draw)
      this._map.removeInteraction(this._draw);
    else
      this._map.addLayer(drawVectorLayer);

    this._draw = new Draw({
      source: drawSource,
      type: type
    });
    this._map.addInteraction(this._draw);
    console.log("draw interaction added", type);
  }
}
