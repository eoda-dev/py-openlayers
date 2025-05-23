import VectorLayer from "ol/layer/Vector";
import TileLayer from "ol/layer/Tile";
import VectorTileLayer from "ol/layer/VectorTile";

import ImageLayer from "ol/layer/Image";
import VectorImageLayer from "ol/layer/VectorImage";

import HeatmapLayer from 'ol/layer/Heatmap.js';

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
    ImageLayer: ImageLayer,
    VectorImageLayer: VectorImageLayer,
    HeatmapLayer: HeatmapLayer
};

// Draw interaction
/*
const drawSource = new VectorSource({ wrapX: false });
const drawVectorLayer = new VectorLayer({
    source: drawSource
});
drawVectorLayer.setProperties({ id: "draw", type: "VectorLayer" });
*/

export { layerCatalog };
