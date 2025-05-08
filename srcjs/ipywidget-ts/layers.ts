import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import WebGLVectorLayer from 'ol/layer/WebGLVector.js';
import WebGLTileLayer from 'ol/layer/WebGLTile.js';

import VectorSource from "ol/source/Vector";

const layerCatalog: LayerCatalog = {
    TileLayer: TileLayer,
    VectorLayer: VectorLayer,
    WebGLVectorLayer: WebGLVectorLayer,
    WebGLTileLayer: WebGLTileLayer
};

// Draw interaction
const drawSource = new VectorSource({ wrapX: false });
const drawVectorLayer = new VectorLayer({
    source: drawSource
});
drawVectorLayer.set("id", "draw-features");

export { layerCatalog, drawSource, drawVectorLayer };
