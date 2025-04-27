// See also https://openlayers.org/en/latest/examples/tooltip-on-hover.html

import { type Map } from "ol";
import Overlay from "ol/Overlay";

function addTooltipOverlayTo(map: Map): { overlay: Overlay; el: HTMLElement } {
    const el = document.createElement("div");
    el.style.cssText = "padding: 5px; background: #efefef; color: black;"
    el.style.visibility = "hidden";
    const overlay = new Overlay({ element: el });
    map.addOverlay(overlay);
    return { overlay, el };
}

function addTooltipTo(map: Map): void {
    const tooltip = addTooltipOverlayTo(map);
    let el = tooltip.el;
    let currentFeature: any = null;
    map.on('pointermove', function (e) {
        if (e.dragging)
            return;
        const feature = map.forEachFeatureAtPixel(e.pixel, function (feature) {
            return feature;
        });
        if (feature) {
            el.style.visibility = "visible";
            // console.log("new pos", e.coordinate, feature.getProperties());
            tooltip.overlay.setPosition(e.coordinate);
            if (feature !== currentFeature) {
                el.innerHTML = feature.get("name")?.toString() || "";
            }
        } else {
            el.style.visibility = "hidden";
            // console.log("HIDE");
        }
        currentFeature = feature;
    });

    map.getTargetElement().addEventListener("pointerleave", () => {
        // console.log("pointerleave");
    });
}

export { addTooltipTo }
