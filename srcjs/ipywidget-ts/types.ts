type SourceCatalog = {
    OSM: any;
    VectorSource: any;
    GeoTIFFSource: any;
    GeoJSONSource: any;
    ImageTileSource: any;
}
type SourceCatalogKey = keyof SourceCatalog;

// ...
type LayerCatalog = {
    TileLayer: any;
    VectorLayer: any;
    WebGLVectorLayer: any;
    WebGLTileLayer: any;
}
type LayerCatalogKey = keyof LayerCatalog;

// ...
type ControlCatalog = {
    [key: string]: any;
}
type ControlCatalogKey = keyof ControlCatalog;

// ... JSON parser
type JSONDef = {
    "@@type": string;
    [key: string]: any;
}

// ...
type TypeCatalog = {
    [key: string]: any;
}

type TypeCatalogKey = keyof TypeCatalog;

// ...
type OLAnyWidgetCall = {
    method: string;
    args: any[];
}
