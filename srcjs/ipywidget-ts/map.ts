import { Map, View } from "ol";
// import * as layers from "ol/layer";
// import * as sources from "ol/source";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import { ViewOptions } from "ol/View";

export default class MapWidget {
  _container: HTMLElement;
  _map: Map;
  constructor(mapElement: HTMLElement, viewOptions: ViewOptions) {
    this._container = mapElement;
    this._map = new Map({
      target: mapElement,
      view: new View(viewOptions),
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
    });
  }
}
