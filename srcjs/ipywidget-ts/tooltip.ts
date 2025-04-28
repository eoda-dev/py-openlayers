// See also https://openlayers.org/en/latest/examples/tooltip-on-hover.html

import { type Map } from "ol";
import Overlay from "ol/Overlay";

function createElement(): HTMLElement {
    const el = document.createElement("div");
    el.style.cssText = "padding: 5px; background-color: #333; color: #fff; border-radius: 4px; z-index: 100;"
    el.style.visibility = "hidden";
    return el;
}

function addTooltipTo(map: Map, prop: string): void {
    let el = createElement();
    const overlay = new Overlay({ element: el });
    map.addOverlay(overlay);
    let currentFeature: any = null;
    map.on('pointermove', function (e) {
        if (e.dragging)
            return;
        const feature = map.forEachFeatureAtPixel(e.pixel, function (feature) {
            return feature;
        });
        if (feature) {
            el.style.visibility = "visible";
            overlay.setPosition(e.coordinate);
            if (feature !== currentFeature) {
                el.innerHTML = feature.get(prop)?.toString() || "";
            }
        } else {
            el.style.visibility = "hidden";
        }
        currentFeature = feature;
    });

    map.getTargetElement().addEventListener("pointerleave", () => {
        el.style.visibility = "hidden";
        currentFeature = undefined;
    });
}

export { addTooltipTo }
