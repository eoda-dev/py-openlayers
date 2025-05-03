import TileLayer from "ol/layer/Tile";
import VectorLayer from "ol/layer/Vector";
import WebGLVectorLayer from 'ol/layer/WebGLVector.js';
import WebGLTileLayer from 'ol/layer/WebGLTile.js';

const layerCatalog: LayerCatalog = {
    TileLayer: TileLayer,
    VectorLayer: VectorLayer,
    WebGLVectorLayer: WebGLVectorLayer,
    WebGLTileLayer: WebGLTileLayer
};

export { layerCatalog };
