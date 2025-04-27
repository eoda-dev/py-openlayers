import Control from "ol/control/Control";

type InfoBoxOptions = {
    target?: string | HTMLElement | undefined;
    html: string;
    cssText?: string;
};

class InfoBox extends Control {
    constructor(options: InfoBoxOptions) {
        const el = document.createElement("div");
        el.className = "ol-control ol-unselectable info-box";
        el.style.cssText = options.cssText || "top: 65px; left: .5em; padding: 5px;";
        el.innerHTML = options.html;
        super({
            element: el,
            target: options.target
        })
    }
}

export { InfoBox };
