import { Map, View } from "ol";

// import * as layers from "ol/layer";
// import * as sources from "ol/source";

import TileLayer from "ol/layer/Tile";
// import OSM from "ol/source/OSM";
import { ViewOptions } from "ol/View";

import { defaults as defaultControls } from 'ol/control/defaults.js';

import { newSource } from "./sources";
import { newLayer } from "./layers";
import { newControl } from "./controls";

// import { MapOptions } from "ol/Map";

// ...
type MyMapOptions = {
  viewOptions: ViewOptions;
  layers: LayerDef[] | undefined;
  controls: any[];
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
    let baseLayers = defaultLayers;
    if (mapOptions.layers !== undefined) {
      baseLayers = mapOptions.layers.map(l => newLayer(l.type, l.options));
    }

    let controls = mapOptions.controls || [];
    controls = controls.map(c => newControl(c.type, c.options));

    // const baseLayers = mapOptions.layers || defaultLayers;
    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: new View(mapOptions.viewOptions),
      controls: defaultControls().extend(controls),
      layers: baseLayers,
    });
  }

  getMap(): Map {
    return this._map;
  }

  // ...
  debugData(data: any): void {
    console.log("debug", data);

    const sources = data?.sources || [];
    for (let s of sources) {
      console.log(s.type, newSource(s.type, s.options));
    }

    const layers: LayerDef[] = data?.layers || [];
    for (let l of layers) {
      console.log(l.type, newLayer(l.type, l.options));
    }
  }
}
