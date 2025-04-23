import { Map, View } from "ol";

// import * as layers from "ol/layer";
// import * as sources from "ol/source";

import TileLayer from "ol/layer/Tile";
// import OSM from "ol/source/OSM";
import { ViewOptions } from "ol/View";

import { newSource } from "./sources";
import { MapOptions } from "ol/Map";

type MyMapOptions = {
  viewOptions: ViewOptions;
  layers: any[] | undefined;
};

const defaultLayers = [
  new TileLayer({
    // source: new OSM(),
    source: newSource("OSM")
  })
];

export default class MapWidget {
  _container: HTMLElement;
  _map: Map;

  constructor(mapElement: HTMLElement, mapOptions: MyMapOptions) {
    const baseLayers = mapOptions.layers || defaultLayers;
    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: new View(mapOptions.viewOptions),
      layers: baseLayers,
    });
  }

  debugData(data: any): void {
    console.log("debug", data);
    const sources = data?.sources || [];
    for (let s of sources) {
      console.log(s.type, newSource(s.type, s.options));
    }
  }
}
