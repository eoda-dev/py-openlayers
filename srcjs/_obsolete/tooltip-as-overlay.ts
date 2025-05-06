// See also https://openlayers.org/en/latest/examples/tooltip-on-hover.html

import { type Map } from "ol";
import { type FeatureLike } from "ol/Feature";
import Overlay from "ol/Overlay";

type FeatureProps = {
    [x: string]: any;
}

function createElement(cssText?: string | undefined): HTMLElement {
    const el = document.createElement("div");
    el.id = "ol-tooltip";
    el.style.cssText = cssText || "padding: 5px; background-color: #333; color: #fff; border-radius: 4px; z-index: 100;"
    el.style.visibility = "hidden";
    return el;
}

function getFeatureProperties(feature: FeatureLike): FeatureProps {
    let { geometry, ...props } = feature.getProperties();
    return props;
}

function addTooltipTo(map: Map, prop: string): void {
    let el = createElement();
    const overlay = new Overlay({ element: el });
    map.addOverlay(overlay);
    let currentFeature: FeatureLike | undefined;
    map.on('pointermove', (e) => {
        if (e.dragging)
            return;
        const feature = map.forEachFeatureAtPixel(e.pixel, (feature) => {
            return feature;
        });
        if (feature) {
            el.style.visibility = "visible";
            overlay.setPosition(e.coordinate);
            if (feature !== currentFeature) {
                console.log("feature props", getFeatureProperties(feature));
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
