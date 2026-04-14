import type { AnyModel } from "@anywidget/types";
import type { Map } from "ol";
import type Feature from "ol/Feature";

import Style from "ol/style/Style";
import Fill from 'ol/style/Fill.js';
import Stroke from 'ol/style/Stroke.js';
import VectorLayer from "ol/layer/Vector";

// Box selection
import { platformModifierKeyOnly } from 'ol/events/condition.js';
import { getWidth } from 'ol/extent.js';
import DragBox from 'ol/interaction/DragBox.js';
import { getTransformFromProjections, transform } from 'ol/proj';

import { featureToGeoJSON } from "./utils";
import VectorSource from "ol/source/Vector";

// TODO: Should be a parameter
const highlightStyle = new Style({
    fill: new Fill({
        color: 'rgba(58, 154, 178,0.7)'
    }),
    stroke: new Stroke({
        // color: 'rgba(241, 27, 0, 0.7)',
        color: "rgba(220, 203, 78, 0.7)",
        // color: "rgba(111, 178, 193, 0.7)",
        width: 2
    })
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
            if (layer instanceof VectorLayer) {
                const source: VectorSource = layer.getSource();
                console.log("source extend", source.getExtent());
                // const features = source.getFeaturesInExtent(extent).filter((feature: Feature) => feature?.getGeometry()?.intersectsExtent(extent));
                source.forEachFeatureIntersectingExtent(extent, (feature: Feature) => {
                    feature.set("layer", layer.get("id"));
                    selected.push(featureToGeoJSON(feature));
                });
                console.log("selected features", selected);
            }
        }
    });


    dragBox.on('boxstart', function () {
        // select.clearSelection();
        selected = [];
    });
}

export { addSelectFeaturesToMap, addBoxSelectionToMap };
