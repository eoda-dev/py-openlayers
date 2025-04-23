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
  const viewOptions = model.get("view_options");
  console.log("viewOptions", viewOptions);
  const mapWidget = new MapWidget(mapElement, viewOptions);
  el.appendChild(mapElement);
}

export default { render };
