import { Map } from "ol";
import { FeatureLike } from "ol/Feature";
import Feature from "ol/Feature";
import Style, { StyleLike } from "ol/style/Style";
import Fill from 'ol/style/Fill.js';
import Stroke from 'ol/style/Stroke.js';
import VectorLayer from "ol/layer/Vector";

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

function addSelectFeaturesToMap(map: Map): void {
    const selected = [] as Feature[];

    map.on('singleclick', function (e) {
        map.forEachFeatureAtPixel(e.pixel, function (feature, layer) {
            const isVectorLayer = layer instanceof VectorLayer;
            console.log("isVectorLayer", isVectorLayer);
            const f = feature as Feature;
            const selIndex = selected.indexOf(f);
            if (selIndex < 0) {
                console.log("push");
                selected.push(f);

                // Does not work for WebGLVectorLayer
                if (isVectorLayer)
                    f.setStyle(highlightStyle);
            } else {
                console.log("delete");
                selected.splice(selIndex, 1);

                // Does not work for WebGLVectorLayer
                if (isVectorLayer)
                    f.setStyle();
            }
        });

        const output = selected.map(f => { return f.getProperties(); });
        console.log(output);
    });
}

export { addSelectFeaturesToMap };
