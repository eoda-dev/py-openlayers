import OSM from "ol/source/OSM";
import VectorSource from "ol/source/Vector";
import GeoTIFFSource from 'ol/source/GeoTIFF.js';
import ImageTileSource from "ol/source/ImageTile";
import { PMTilesVectorSource, PMTilesRasterSource } from "ol-pmtiles";

const sourceCatalog: SourceCatalog = {
    OSM: OSM,
    VectorSource: VectorSource,
    GeoTIFFSource: GeoTIFFSource,
    GeoJSONSource: VectorSource,
    ImageTileSource: ImageTileSource,
    PMTilesVectorSource: PMTilesVectorSource,
    PMTilesRasterSource: PMTilesRasterSource
};

export { sourceCatalog };
