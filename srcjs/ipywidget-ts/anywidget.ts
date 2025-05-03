import "ol/ol.css";

import MapWidget from "./map";
import { parseClickEvent } from "./utils";

// --- Types
import type { AnyModel } from "@anywidget/types";

// --- Main function
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
  const mapWidget = (window as any).anywidgetMapWidget = new MapWidget(mapElement, mapOptions);

  model.set("map_created", true);
  model.save_changes();

  const calls: OLAnyWidgetCall[] = model.get("calls");
  console.log("calls", calls);
  for (let call of calls) {
    // @ts-expect-error
    mapWidget[call.method](...call.args);
  }

  const map = mapWidget.getMap();
  /*
  map.on("click", (e) => {
    const info = parseClickEvent(e);
    console.log(info);
    model.set("map_clicked", info);
    model.save_changes();
  });
  */

  model.on("msg:custom", (msg: OLAnyWidgetCall) => {
    console.log("thanx for your message", msg);

    try {
      // @ts-expect-error
      mapWidget[msg.method](...msg.args);
    } catch (error) {
      console.log("error in anywidget msg call", error);
    }
  });

  el.appendChild(mapElement);
}

export default { render };
