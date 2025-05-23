import OSM from "ol/source/OSM";
import VectorSource from "ol/source/Vector";
import VectorTileSource from 'ol/source/VectorTile.js';
import GeoTIFFSource from 'ol/source/GeoTIFF.js';
import ImageTileSource from "ol/source/ImageTile";
import TileJSON from 'ol/source/TileJSON.js';
import { PMTilesVectorSource, PMTilesRasterSource } from "ol-pmtiles";

const sourceCatalog: SourceCatalog = {
    OSM: OSM,
    VectorSource: VectorSource,
    VectorTileSource: VectorTileSource,
    GeoTIFFSource: GeoTIFFSource,
    GeoJSONSource: VectorSource,
    ImageTileSource: ImageTileSource,
    TileJSON: TileJSON,
    PMTilesVectorSource: PMTilesVectorSource,
    PMTilesRasterSource: PMTilesRasterSource
};

export { sourceCatalog };
