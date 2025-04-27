import { Map } from "ol"
import { Pixel } from "ol/pixel";
import { FeatureLike } from "ol/Feature";

const info = document.createElement("div");

/*
function addTooltipTo(map: Map): void {
    let currentFeature: FeatureLike | undefined;
    const displayFeatureInfo = function (pixel: Pixel, target: EventTarget | null) {
        const feature = target.closest('.ol-control')
            ? undefined
            : map.forEachFeatureAtPixel(pixel, function (feature) {
                return feature;
            });
        if (feature) {
            info.style.left = pixel[0] + 'px';
            info.style.top = pixel[1] + 'px';
            if (feature !== currentFeature) {
                info.style.visibility = 'visible';
                info.innerText = "XYZ"; // feature.get('ECO_NAME');
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
*/