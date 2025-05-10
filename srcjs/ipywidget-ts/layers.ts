import VectorLayer from "ol/layer/Vector";
import TileLayer from "ol/layer/Tile";
import VectorTileLayer from "ol/layer/VectorTile";

import ImageLayer from "ol/layer/Image";

// WebGL
import WebGLVectorLayer from 'ol/layer/WebGLVector.js';
import WebGLTileLayer from 'ol/layer/WebGLTile.js';
import WebGLVectorTileLayer from 'ol/layer/WebGLVectorTile.js';

import VectorSource from "ol/source/Vector";

const layerCatalog: LayerCatalog = {
    TileLayer: TileLayer,
    VectorLayer: VectorLayer,
    WebGLVectorLayer: WebGLVectorLayer,
    WebGLTileLayer: WebGLTileLayer,
    VectorTileLayer: VectorTileLayer,
    WebGLVectorTileLayer: WebGLVectorTileLayer,
    ImageLayer: ImageLayer
};

// Draw interaction
const drawSource = new VectorSource({ wrapX: false });
const drawVectorLayer = new VectorLayer({
    source: drawSource
});
drawVectorLayer.set("id", "draw-features");
drawVectorLayer.set("type", "VectorLayer");

export { layerCatalog, drawSource, drawVectorLayer };
