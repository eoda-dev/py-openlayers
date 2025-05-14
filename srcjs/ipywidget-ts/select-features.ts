import type { AnyModel } from "@anywidget/types";
import type { Map } from "ol";
import type Feature from "ol/Feature";

import Style from "ol/style/Style";
import Fill from 'ol/style/Fill.js';
import Stroke from 'ol/style/Stroke.js';
import VectorLayer from "ol/layer/Vector";

import { featureToGeoJSON } from "./utils";

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

export { addSelectFeaturesToMap };
