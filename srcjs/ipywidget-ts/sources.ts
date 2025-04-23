import OSM from "ol/source/OSM";
import VectorSource from "ol/source/Vector";

import { GeoJSON } from "ol/format";

// import { OSM } from "ol/source";

const sources = {
    OSM: OSM,
    VectorSource: VectorSource
};

type SourceKey = keyof typeof sources;
type SourceOptions = any;

function parseSourceOptions(options: SourceOptions): SourceOptions {
    if (options.format === "geojson") {
        options.format = new GeoJSON()
    }

    return options;
}

function newSource(type: SourceKey, options?: SourceOptions): any {
    options = options ? parseSourceOptions(options) : options;
    const source = new sources[type](options)
    return source;
}

export { newSource, sources };
