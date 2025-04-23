import { type AnyModel } from "@anywidget/types";

// import "./style.css";
import "ol/ol.css";

import MapWidget from "./map";

function render({ model, el }: { model: AnyModel; el: HTMLElement }): void {
  console.log("Welcome to anywidget", el);
  // el.innerHTML = "Welcome to anywidget";
  // const calls = model.get("calls");
  // console.log(calls);
  const height = model.get("height") || "400px";
  console.log("height", height);
  const mapElement = document.createElement("div");
  mapElement.id = "ol-map-widget";
  mapElement.style.height = height;
  // ...
  const mapOptions = model.get("map_options");
  console.log("mapOptions", mapOptions);
  const mapWidget = new MapWidget(mapElement, mapOptions);

  // ...
  const debugData = model.get("debug_data");
  mapWidget.debugData(debugData);

  el.appendChild(mapElement);
}

export default { render };
