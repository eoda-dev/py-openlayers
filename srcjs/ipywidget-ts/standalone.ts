import "ol/ol.css";

import MapWidget from "./map";
import { MyMapOptions } from ".";

const MAP_CONTAINER = "map";

(window as any).renderOLMapWidget = (mapOptions: MyMapOptions) => {
    // mapOptions.viewOptions = mapOptions.viewOptions || { center: [0, 0] };
    console.log("render OL-MapWidget", mapOptions);
    const mapElement = document.getElementById(MAP_CONTAINER) || document.createElement("div");
    console.log("el", mapElement);
    const mapWidget = new MapWidget(mapElement, mapOptions);
    const map = mapWidget.getMap();

    console.log("calls", mapOptions.calls);
    if (mapOptions.calls) {
        for (let call of mapOptions.calls) {
            // @ts-expect-error
            mapWidget[call.method](...call.args);
        }
    }
};
