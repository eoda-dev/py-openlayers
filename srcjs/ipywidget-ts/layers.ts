import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import WebGLVectorLayer from 'ol/layer/WebGLVector.js';
import WebGLTileLayer from 'ol/layer/WebGLTile.js';
// import BaseLayer from "ol/layer/Base";

import { newSource } from "./sources";

const layerCatalog: LayerCatalog = {
    TileLayer: TileLayer,
    VectorLayer: VectorLayer,
    WebGLVectorLayer: WebGLVectorLayer,
    WebGLTileLayer: WebGLTileLayer
};

function newLayer(type: LayerKey, options: LayerOptions): any {
    const sourceDef = options.source;
    options.source = newSource(sourceDef.type, sourceDef.options);
    const layer = new layerCatalog[type](options)
    return layer;
}

export { newLayer, layerCatalog };
