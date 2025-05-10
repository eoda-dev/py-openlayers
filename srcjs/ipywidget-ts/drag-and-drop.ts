// See https://openlayers.org/en/latest/examples/drag-and-drop.html
// ---
import type { Map } from "ol";
import type FeatureFormat from "ol/format/Feature";

import GPX from 'ol/format/GPX.js';
import GeoJSON from 'ol/format/GeoJSON.js';
import IGC from 'ol/format/IGC.js';
import KML from 'ol/format/KML.js';
import TopoJSON from 'ol/format/TopoJSON.js';
import DragAndDrop from 'ol/interaction/DragAndDrop.js';
import VectorSource from 'ol/source/Vector.js';
import VectorLayer from 'ol/layer/Vector.js';
import { FlatStyle } from "ol/style/flat";

const defaultFormats = [
    new GPX(),
    new GeoJSON(),
    new IGC(),
    new KML(),
    new TopoJSON(),
];

function addDragAndDropToMap(map: Map, formats?: FeatureFormat[], style?: FlatStyle): void {
    let dragAndDropInteraction: any;

    function setInteraction() {
        if (dragAndDropInteraction) {
            map.removeInteraction(dragAndDropInteraction);
        }
        dragAndDropInteraction = new DragAndDrop({
            formatConstructors: formats || defaultFormats
        });
        dragAndDropInteraction.on('addfeatures', function (event: any) {
            const vectorSource = new VectorSource({
                features: event.features,
            });
            const vectorLayer = new VectorLayer({
                source: vectorSource,
                style: style || undefined
            });
            // vectorLayer.set("id", `drag-and-drop-${Date.now()}`);
            // vectorLayer.set("type", "VectorLayer");
            vectorLayer.setProperties({
                id: `drag-and-drop-${Date.now()}`,
                type: "VectorLayer"
            });
            map.addLayer(vectorLayer);
            map.getView().fit(vectorSource.getExtent());
        });
        map.addInteraction(dragAndDropInteraction);
    }
    setInteraction();
}

export { addDragAndDropToMap };
