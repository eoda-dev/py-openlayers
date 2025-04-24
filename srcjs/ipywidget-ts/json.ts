import { layerCatalog } from "./layers"
import { sourceCatalog } from "./sources"
import { controlCatalog } from "./controls"

// const LAYER_IDENTIFIER = "@layer="
// const SOURCE_INDENTIFIER = "@source="
// const CONTROL_IDENTIFIER = "@control="


class JSONConverter {
    _catalog: any

    // constructor(layerCatalog?: LayerCatalog, sourceCatalog?: SourceCatalog, controlCatalog?: ControlCatalog) {
    constructor() {
        this._catalog = { ...controlCatalog, ...layerCatalog, ...sourceCatalog };
    }

    getType(jsonDef: JSONDef): any {

    }

    parseOptions(options: any): any {

    }

    parse(jsonDef: JSONDef): any {
        // console.log(this._catalog);
        return new this._catalog[jsonDef["@@type"]](jsonDef);
    }
}

export { JSONConverter }