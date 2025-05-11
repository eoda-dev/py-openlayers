import Control from "ol/control/Control";

type DrawOptions = {
    target?: string | HTMLElement | undefined;
    cssText?: string;
};


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

class DrawControl extends Control {
    constructor(options: DrawOptions) {
        const el = document.createElement("div");
        el.className = "ol-control ol-unselectable draw-control";
        el.style.cssText = options.cssText || "top: .5em; left: 35px; padding: 5px;";
        el.appendChild(createSelectElement());
        super({
            element: el,
            target: options.target
        })
    }
}

export { DrawControl };
