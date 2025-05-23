/**
 * See https://openlayers.org/en/latest/examples/draw-features.html
 * and https://openlayers.org/en/latest/examples/draw-and-modify-features.html
 * */
import type { Map } from "ol";
import type { Type as GeomType } from "ol/geom/Geometry";

import Control from "ol/control/Control";

import Draw from "ol/interaction/Draw";
import Modify from 'ol/interaction/Modify.js';
import Snap from 'ol/interaction/Snap.js';

import VectorSource from "ol/source/Vector";
import VectorLayer from "ol/layer/Vector";

import { featureToGeoJSON } from "../utils";

type DrawOptions = {
    target?: string | HTMLElement | undefined;
    cssText?: string;
};

let draw: Draw;
let snap: Snap;

const source = new VectorSource({ wrapX: false });
/*
source.on("addfeature", (e) => {
    const features = source.getFeatures().map(f => featureToGeoJSON(f));
    console.log("draw features", features);
});
*/
const modify = new Modify({ source: source });
const vectorLayer = new VectorLayer({
    source: source,
    zIndex: 1000,
});
vectorLayer.setProperties({ id: "draw", type: "VectorLayer" });

const selectOptions = [
    { name: "Point", value: "Point" },
    { name: "Line", value: "LineString" },
    { name: "Polygon", value: "Polygon" },
    { name: "Circle", value: "Circle" },
    { name: "None", value: "None" }
];

function createSelectElement(): HTMLSelectElement {
    const select = document.createElement("select");
    select.style.padding = "2px";
    for (const item of selectOptions) {
        const option = document.createElement("option");
        option.value = item.value;
        option.text = item.name;
        select.appendChild(option);
    }
    return select;
}

function toggleDrawInteraction(map: Map, select: HTMLSelectElement): void {
    map.addInteraction(modify);

    function addInteraction() {
        const value = select.value;
        if (value === "None")
            return;

        draw = new Draw({
            source: source,
            type: value as GeomType

        });
        map.addInteraction(draw);
        snap = new Snap({ source: source });
        map.addInteraction(snap);
    }

    select.onchange = () => {
        map.removeInteraction(draw);
        map.removeInteraction(snap);
        addInteraction();
    };

    addInteraction();
}

class DrawControl extends Control {
    constructor(options?: DrawOptions) {
        options = options || {};
        const el = document.createElement("div");
        el.className = "ol-draw ol-control ol-unselectable";
        el.style.cssText = options.cssText || "top: .5em; left: 35px;";
        super({
            element: el,
            target: options.target
        });
        this.setProperties({ id: "draw", type: "DrawControl" });
    }

    onAdd(): void {
        const map = this.getMap();
        map?.addLayer(vectorLayer);
        const select = createSelectElement();

        if (map) {
            toggleDrawInteraction(map, select);
            this.element.appendChild(select);
        }
    }

    getDraw(): Draw | undefined {
        return draw;
    }

    getSnap(): Snap | undefined {
        return snap;
    }

    getGeoJSONFeatures(): any[] {
        return source.getFeatures().map(f => featureToGeoJSON(f));
    }

    getLayer(): VectorLayer {
        return vectorLayer;
    }
}

export { DrawControl };
