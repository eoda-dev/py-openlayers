import OSM from "ol/source/OSM";
import VectorSource from "ol/source/Vector";
import GeoTIFFSource from 'ol/source/GeoTIFF.js';
import ImageTileSource from "ol/source/ImageTile";

// import { GeoJSON } from "ol/format";

// import { OSM } from "ol/source";

const sourceCatalog: SourceCatalog = {
    OSM: OSM,
    VectorSource: VectorSource,
    GeoTIFFSource: GeoTIFFSource,
    GeoJSONSource: VectorSource,
    ImageTileSource: ImageTileSource
};

/*
function parseSourceOptions(options: SourceOptions): SourceOptions {
    if (options.format === "geojson") {
        options.format = new GeoJSON()
    }

    return options;
}
*/

/*
function newSource(type: SourceCatalogKey, options?: SourceOptions): any {
    options = options ? parseSourceOptions(options) : options;
    const source = new sourceCatalog[type](options)
    return source;
}
*/

export { sourceCatalog };
