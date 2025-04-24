import { type AnyModel } from "@anywidget/types";
import { transform as transformProj } from "ol/proj";
import { parseClickEvent } from "./utils";

// import "./style.css";
import "ol/ol.css";

import MapWidget from "./map";
import TileLayer from "ol/layer/Tile";

function render({ model, el }: { model: AnyModel; el: HTMLElement }): void {
  console.log("Welcome to ol-anywidget", el);

  const height = model.get("height") || "400px";
  console.log("height", height);
  const mapElement = document.createElement("div");
  mapElement.id = "ol-map-widget";
  mapElement.style.height = height;
  // ...
  const mapOptions = model.get("map_options");
  console.log("mapOptions", mapOptions);
  const mapWidget = new MapWidget(mapElement, mapOptions);

  const map = mapWidget.getMap();
  map.on("click", (e) => {
    const info = parseClickEvent(e);
    console.log(info);
    model.set("map_clicked", info);
    model.save_changes();
  });

  // ...
  const debugData = model.get("debug_data");
  mapWidget.debugData(debugData);

  const obj = mapWidget.testJSONDef({
    "@@type": "ScaleLineControl",
    bar: true
  });
  console.log(obj);
  map.addControl(obj);

  // layer
  const l = mapWidget.testJSONDef({
    "@@type": "TileLayer",
    "source": {
      "@@type": "OSM"
    }
  }) as TileLayer;
  console.log("layer", l.getSource()?.getAttributions());
  map.addLayer(l);

  el.appendChild(mapElement);
}

export default { render };
