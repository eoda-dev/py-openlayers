import { Map, View } from "ol";
import { ViewOptions } from "ol/View";

import TileLayer from "ol/layer/Tile";

import OSM from "ol/source/OSM";

import { defaults as defaultControls } from 'ol/control/defaults.js';
// import { MapOptions } from "ol/Map";

import { JSONConverter } from "./json";

// import { populatedPlacesLayer } from "./test-json-converter";
import BaseLayer from "ol/layer/Base";

// ...
type MyMapOptions = {
  viewOptions: ViewOptions;
  layers: JSONDef[] | undefined;
  controls: JSONDef[] | undefined;
};

//
type LayerStore = {
  [key: string]: BaseLayer
}


const jsonConverter = new JSONConverter();

const defaultLayers = [
  new TileLayer({
    source: new OSM()
  })
];

export default class MapWidget {
  _container: HTMLElement;
  _map: Map;
  _layerStore: LayerStore = {};

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions) {
    let baseLayers: BaseLayer[] = [] // defaultLayers;
    if (mapOptions.layers !== undefined) {
      // baseLayers = mapOptions.layers.map(layerJSONDef => jsonConverter.parse(layerJSONDef));
      for (let layerJSONDef of mapOptions.layers) {
        const layer = jsonConverter.parse(layerJSONDef);
        baseLayers.push(layer);
        this._layerStore[layerJSONDef.id] = layer;
        // console.log(this._layerStore);
      }
    }

    // test
    // baseLayers.push(jsonConverter.parse(populatedPlacesLayer));

    let baseControls = [];
    if (mapOptions.controls !== undefined) {
      baseControls = mapOptions.controls.map(controlJSONDef => jsonConverter.parse(controlJSONDef));
    }

    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: new View(mapOptions.viewOptions),
      controls: defaultControls().extend(baseControls),
      layers: baseLayers,
    });
  }

  getMap(): Map {
    return this._map;
  }

  addLayer(layerJSONDef: JSONDef): void {
    const layer = jsonConverter.parse(layerJSONDef);
    this._map.addLayer(layer);
    this._layerStore[layerJSONDef.id] = layer;
  }

  removeLayer(layerId: string): void {
    const layer = this._layerStore[layerId];
    if (layer === undefined) return;

    this._map.removeLayer(layer);
    delete this._layerStore[layerId];
    console.log("layer", layerId, "removed");
    console.log(this._layerStore);

  }

  addControl(controlJSONDef: JSONDef): void {
    const control = jsonConverter.parse(controlJSONDef);
    this._map.addControl(control);
  }

  testJSONDef(jsonDef: JSONDef): any {
    return jsonConverter.parse(jsonDef);
  }

  // ...
  debugData(data: any): void {
  }
}
