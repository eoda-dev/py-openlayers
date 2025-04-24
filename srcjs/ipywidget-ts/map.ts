import { Map, View } from "ol";
import { ViewOptions } from "ol/View";

import TileLayer from "ol/layer/Tile";

import OSM from "ol/source/OSM";

import { defaults as defaultControls } from 'ol/control/defaults.js';
// import { MapOptions } from "ol/Map";

import { JSONConverter } from "./json";

// ...
type MyMapOptions = {
  viewOptions: ViewOptions;
  layers: JSONDef[] | undefined;
  controls: JSONDef[] | undefined;
};

const jsonConverter = new JSONConverter();

const defaultLayers = [
  new TileLayer({
    source: new OSM()
  })
];

export default class MapWidget {
  _container: HTMLElement;
  _map: Map;

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions) {
    let baseLayers = [] // defaultLayers;
    if (mapOptions.layers !== undefined) {
      baseLayers = mapOptions.layers.map(layerJSONDef => jsonConverter.parse(layerJSONDef));
    }

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
