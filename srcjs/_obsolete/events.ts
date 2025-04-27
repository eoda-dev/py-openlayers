import type { Map } from "ol";
import Select from 'ol/interaction/Select.js';
import { singleClick, pointerMove, doubleClick, altKeyOnly } from "ol/events/condition";

let props: any = null;

const select = new Select({ condition: pointerMove });


function addFeatureEventListenerTo(map: Map): void {
    map.addInteraction(select);
    // let id: any = null;
    select.on("select", (e) => {
        const x = e.target.getFeatures().item(0);
        if (x !== undefined) {
            // id = x.getProperties().id;
            console.log("seleted", x.getProperties());
        }

    });


    /*
    map.on('pointermove', function (e) {
        if (props !== null) {
            console.log("props", props);
            props = null;
        }
        map.forEachFeatureAtPixel(e.pixel, function (feature) {
            props = feature.getProperties()
            // console.log("feature", feature.getProperties());
        });

        // if (props !== null) console.log("props", props);
        // else console.log("nothing");
    })
        */
}

export { addFeatureEventListenerTo };
