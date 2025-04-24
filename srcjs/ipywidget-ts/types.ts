type SourceCatalog = {
    OSM: any;
    VectorSource: any;
    GeoTIFFSource: any;
}
type SourceKey = keyof SourceCatalog;
type SourceOptions = any;
type SourceDef = {
    type: SourceKey;
    options: any;
}

type LayerCatalog = {
    TileLayer: any;
    VectorLayer: any;
    WebGLVectorLayer: any;
    WebGLTileLayer: any;
}
type LayerKey = keyof LayerCatalog;
type LayerOptions = {
    source: SourceDef;
    [key: string]: any;
}
type LayerDef = {
    type: LayerKey;
    options: LayerOptions;
}

type Controls = {
    [key: string]: any;
}
