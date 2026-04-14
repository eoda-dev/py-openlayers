import type { AnyModel } from "@anywidget/types";
import type { Map } from "ol";
import type Feature from "ol/Feature";

import Style from "ol/style/Style";
import Fill from 'ol/style/Fill';
import Stroke from 'ol/style/Stroke';
import Circle from "ol/style/Circle";
import VectorLayer from "ol/layer/Vector";
import WebGLVectorLayer from "ol/layer/WebGLVector";
import VectorSource from "ol/source/Vector";

// Box selection
import { platformModifierKeyOnly } from 'ol/events/condition';
// import { getWidth } from 'ol/extent.js';
import DragBox from 'ol/interaction/DragBox';
// import { getTransformFromProjections, transform } from 'ol/proj';

import { featureToGeoJSON } from "./utils";

const fill = new Fill({
    color: 'rgba(58, 154, 178,0.7)'
});
const stroke = new Stroke({
    color: "rgba(220, 203, 78, 0.7)",
    width: 2
});

// TODO: Should be a parameter
const highlightStyle = new Style({
    image: new Circle({
        fill: fill,
        stroke: stroke,
        radius: 5,
    }),
    fill: fill,
    stroke: stroke
});

// TODO: Setting new style only works for 'VectorLayer'
// For 'WebGLVectorLayer' we need to add complete highlight-layer on top of the current one 
function addSelectFeaturesToMap(map: Map, model?: AnyModel): void {
    const selected = [] as Feature[];

    map.on('singleclick', function (e) {
        map.forEachFeatureAtPixel(e.pixel, function (feature, layer) {
            const isVectorLayer = layer instanceof VectorLayer;

            // console.log("isVectorLayer", isVectorLayer);
            const f = feature as Feature;
            f.set("layer", layer.get("id"));
            const selIndex = selected.indexOf(f);
            if (selIndex < 0) {
                console.log("push");
                selected.push(f);
                if (isVectorLayer)
                    f.setStyle(highlightStyle);
            } else {
                console.log("delete");
                selected.splice(selIndex, 1);
                if (isVectorLayer)
                    f.setStyle();
            }
        });
        const output = selected.map(f => featureToGeoJSON(f));
        // console.log("model", model);
        if (model) {
            // model.set("features_selected", output);
            model.set("features", { selected: output });
            model.save_changes();
        } else
            console.log(output);
    });
}

function addBoxSelectionToMap(map: Map, model?: AnyModel): void {
    console.warn("Box selection is still experimental.");

    let selected = [] as Feature[];

    const dragBox = new DragBox({
        condition: platformModifierKeyOnly,
    });
    map.addInteraction(dragBox);
    dragBox.on('boxend', function () {
        const extent = dragBox.getGeometry().transform('EPSG:3857', 'EPSG:4326').getExtent();
        console.log("box extent", extent);
        //
        for (let layer of map.getLayers().getArray()) {
            if (layer instanceof VectorLayer || layer instanceof WebGLVectorLayer) {
                const source: VectorSource = layer.getSource();
                console.log("source extend", source.getExtent());
                // const features = source.getFeaturesInExtent(extent).filter((feature: Feature) => feature?.getGeometry()?.intersectsExtent(extent));
                source.forEachFeatureIntersectingExtent(extent, (feature: Feature) => {
                    feature.set("layer", layer.get("id"));
                    selected.push(feature);
                    if (layer instanceof VectorLayer) {
                        feature.setStyle(highlightStyle);
                    }
                });
                const output = selected.map(f => featureToGeoJSON(f));
                console.log("selected features", output);
                if (model) {
                    model.set("features", { selected: output });
                    model.save_changes();
                }
            }
        }
    });


    dragBox.on('boxstart', function () {
        selected.forEach((f: Feature) => { f.setStyle(); });
        if (model) {
            model.set("features", {});
            model.save_changes();
        }
        selected = [];
    });
}

export { addSelectFeaturesToMap, addBoxSelectionToMap };
