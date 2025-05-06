/*
taken from https://openlayers.org/en/latest/examples/tooltip-on-hover.html
*/
import { Map } from "ol";
import type { FeatureLike } from "ol/Feature";
import type { Pixel } from "ol/pixel";

import mustache from "mustache";

import { getFeatureProperties } from "./utils";

/*
#info {
    position: absolute;
    display: inline-block;
    height: auto;
    width: auto;
    z-index: 100;
    background-color: #333;
    color: #fff;
    text-align: center;
    border-radius: 4px;
    padding: 5px;
    left: 50%;
    transform: translateX(3%);
    visibility: hidden;
    pointer-events: none;
}
*/

const info = document.createElement("div");
info.style.position = "absolute";
info.style.display = "inline-block";
info.style.height = "auto";
info.style.width = "auto";
info.style.zIndex = "100";
info.style.backgroundColor = "#333";
info.style.color = "#fff";
// info.style.textAlign = "center";
info.style.borderRadius = "4px";
info.style.padding = "7px";
info.style.left = "50%";
// info.style.transform = "translateX(3%)";
info.style.visibility = "hidden";
info.style.pointerEvents = "none";

function renderFeatureProperties(feature: FeatureLike, template: string | null): string {
    const properties = getFeatureProperties(feature);
    if (template)
        return mustache.render(template, properties);

    return Object.keys(properties).map((key) => `${key}: ${properties[key]}`).join("</br>");
}

function addTooltipToMap(map: Map, template: string | null): void {
    info.id = "ol-tooltip";
    map.getTargetElement().appendChild(info);
    console.log("tooltip element added", info);

    let currentFeature: FeatureLike | undefined;
    const displayFeatureInfo = function (pixel: Pixel, target: EventTarget | null) {
        // @ts-expect-error
        const feature = target.closest('.ol-control')
            ? undefined
            : map.forEachFeatureAtPixel(pixel, function (feature) {
                return feature;
            });
        if (feature) {
            // console.log("feature props", getFeatureProperties(feature));
            info.style.left = (pixel[0] + 15) + 'px';
            info.style.top = pixel[1] + 'px';
            if (feature !== currentFeature) {
                info.style.visibility = 'visible';
                info.innerHTML = renderFeatureProperties(feature, template);
            }
        } else {
            info.style.visibility = 'hidden';
        }
        currentFeature = feature;
    };

    map.on('pointermove', function (evt) {
        if (evt.dragging) {
            info.style.visibility = 'hidden';
            currentFeature = undefined;
            return;
        }
        displayFeatureInfo(evt.pixel, evt.originalEvent.target);
    });

    map.on('click', function (evt) {
        displayFeatureInfo(evt.pixel, evt.originalEvent.target);
    });

    map.getTargetElement().addEventListener('pointerleave', function () {
        currentFeature = undefined;
        info.style.visibility = 'hidden';
    });
}

export { addTooltipToMap };
