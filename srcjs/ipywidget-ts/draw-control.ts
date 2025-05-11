import type { Map } from "ol";

import Control from "ol/control/Control";
import Draw from "ol/interaction/Draw";
import VectorSource from "ol/source/Vector";
import VectorLayer from "ol/layer/Vector";

type DrawOptions = {
    target?: string | HTMLElement | undefined;
    cssText?: string;
};

const source = new VectorSource({ wrapX: false });

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
    for (const item of selectOptions) {
        const option = document.createElement("option");
        option.value = item.value;
        option.text = item.name;
        select.appendChild(option);
    }
    return select;
}

function x(map: Map, select: HTMLSelectElement): void {
    let draw: Draw;

    function addInteraction() {
        const value = select.value;
        if (value !== 'None') {
            draw = new Draw({
                source: source,

                // @ts-expect-error
                type: select.value

            });
            map.addInteraction(draw);
        }
    }

    select.onchange = function () {
        map.removeInteraction(draw);
        addInteraction();
    };
    addInteraction();
}

class DrawControl extends Control {
    constructor(options?: DrawOptions) {
        options = options || {};
        const el = document.createElement("div");
        el.className = "ol-control ol-unselectable draw-control";
        el.style.cssText = options.cssText || "top: .5em; left: 35px; padding: 5px;";
        super({
            element: el,
            target: options.target
        })

        // const map = this.getMap();
        // console.log("map", map);
        // map?.addLayer(vectorLayer);

        // const select = createSelectElement();
        // ts-expect-error
        // x(map, select);
        // el.appendChild(select);
        // this.y()
    }

    y(): void {
        console.log("map", this.getMap());
        const map = this.getMap();
        map?.addLayer(vectorLayer);
        const select = createSelectElement();

        // @ts-expect-error
        x(map, select);
        this.element.appendChild(select);

    }
}

export { DrawControl };
