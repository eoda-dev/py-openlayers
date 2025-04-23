type Sources = {
    OSM: any;
    VectorSource: any;
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
