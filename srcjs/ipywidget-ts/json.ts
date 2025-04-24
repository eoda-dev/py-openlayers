import { layerCatalog } from "./layers"
import { sourceCatalog } from "./sources"
import { controlCatalog } from "./controls"

import { GeoJSON } from "ol/format";

class JSONConverter {
    _catalog: any

    // constructor(layerCatalog?: LayerCatalog, sourceCatalog?: SourceCatalog, controlCatalog?: ControlCatalog) {
    constructor() {
        this._catalog = { ...controlCatalog, ...layerCatalog, ...sourceCatalog, GeoJSON };
    }

    getType(jsonDef: JSONDef): any {

    }

    parseOptions(options: JSONDef): any {
        let parsedOptions = {} as any;
        for (let key in options) {
            const option = options[key];
            if (typeof option === "object" && option["@@type"] !== undefined) {
                parsedOptions[key] = this.parse(option);
            }
            else if (key !== "@@type") {
                parsedOptions[key] = option;
            }
        }

        return parsedOptions;
    }

    parse(jsonDef: JSONDef): any {
        // console.log(this._catalog);
        const parsedOptions = this.parseOptions(jsonDef);
        console.log("parsedOptions", parsedOptions);
        return new this._catalog[jsonDef["@@type"]](parsedOptions);
    }
}

export { JSONConverter }
