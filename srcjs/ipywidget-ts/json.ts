import { layerCatalog } from "./layers"
import { sourceCatalog } from "./sources"
import { controlCatalog } from "./controls"

import { GeoJSON, KML, GPX, TopoJSON, IGC, MVT } from "ol/format";
import { View } from "ol";

import { TYPE_IDENTIFIER, GEOJSON_IDENTIFIER } from "./constants";

// import Feature from 'ol/Feature.js';
// import { Polygon, Point, LineString, Circle } from "ol/geom";

type CallableCatalog = {
    [key: string]: any;
};

class JSONConverter {
    _catalog: CallableCatalog;

    constructor(catalog?: CallableCatalog) {
        this._catalog = catalog || {
            ...controlCatalog,
            ...layerCatalog,
            ...sourceCatalog,
            GeoJSON, KML, GPX, TopoJSON, IGC, MVT,
            View
        };
    }

    // TODO: Remove, not needed anymore
    /*
    moveTypeDefToTop(options: JSONDef): JSONDef {
        let sortedOptions = {} as any
        Object.keys(options).sort().forEach(key => sortedOptions[key] = options[key]);
        console.log("sortedOptions", sortedOptions);
        return sortedOptions;
    }
    */

    parseOptions(options: JSONDef): any {
        let parsedOptions = {} as any;

        // for (let key in this.moveTypeDefToTop(options)) {
        for (const key in options) {
            const option = options[key];
            if (Array.isArray(option) && typeof option[0] === "object") {
                console.log("Parse items of array");
                // parsedOptions[key] = option.map(item => this.parse(item));
                parsedOptions[key] = option.map(item => item[TYPE_IDENTIFIER] ? this.parse(item) : this.parseOptions(item));
            }
            // else if (typeof option === "object" && option[TYPE_IDENTIFIER] !== undefined) {
            else if (option instanceof Object && option[TYPE_IDENTIFIER]) {
                // console.log("type detected", option["@@type"], this._catalog[option["@@type"]]);
                parsedOptions[key] = this.parse(option);
            }
            // else if (key !== "@@type" && key !== "@@geojson") {
            else if (![TYPE_IDENTIFIER, GEOJSON_IDENTIFIER].includes(key)) {
                parsedOptions[key] = option;
            }
        }

        return parsedOptions;
    }

    parse(jsonDef: JSONDef): any {
        const parsedOptions = this.parseOptions(jsonDef);
        console.log("parsed options", parsedOptions);
        console.log("type detected", jsonDef[TYPE_IDENTIFIER]);
        return new this._catalog[jsonDef[TYPE_IDENTIFIER]](parsedOptions);
    }
}

export { JSONConverter };
