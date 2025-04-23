import OSM from "ol/source/OSM";
import VectorSource from "ol/source/Vector";

// import { OSM } from "ol/source";

const sources = {
    OSM: OSM,
    VectorSource: VectorSource
};

type SourceKey = keyof typeof sources;
type SourceOptions = object;

function parseSourceOptions(options: SourceOptions): SourceOptions {
    return options;
}

function newSource(type: SourceKey, options?: SourceOptions): any {
    options = options ? parseSourceOptions(options) : options;
    const source = new sources[type](options)
    return source;
}

export { newSource, sources };
