import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import WebGLVectorLayer from 'ol/layer/WebGLVector.js';
// import BaseLayer from "ol/layer/Base";

import { newSource } from "./sources";

// TODO: Move to types
const layers: Layers = {
    TileLayer: TileLayer,
    VectorLayer: VectorLayer,
    WebGLVectorLayer: WebGLVectorLayer
};

// type LayerKey = keyof typeof layers;
// type LayerOptions = any;

function newLayer(type: LayerKey, options: LayerOptions): any {
    const sourceDef = options.source;
    options.source = newSource(sourceDef.type, sourceDef.options);
    const layer = new layers[type](options)
    return layer;
}

export { newLayer };
