type Sources = {
    OSM: any;
    VectorSource: any;
    GeoTIFFSource: any;
}
type SourceKey = keyof Sources;
type SourceOptions = any;
type SourceDef = {
    type: SourceKey;
    options: any;
}

type Layers = {
    TileLayer: any;
    VectorLayer: any;
    WebGLVectorLayer: any;
    WebGLTileLayer: any;
}
type LayerKey = keyof Layers;
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
