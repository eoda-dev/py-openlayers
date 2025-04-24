const scaleLineControl = {
    "@@type": "ScaleLineControl",
    bar: true
};

const baseLayer = {
    "@@type": "TileLayer",
    "source": {
        "@@type": "OSM"
    }
};

const webglVectorLayer = {
    "@@type": "WebGLVectorLayer",
    source: {
        "@@type": "VectorSource",
        url: "https://openlayers.org/data/vector/ecoregions.json",
        format: {
            "@@type": "GeoJSON"
        }
    },
    "style": {
        'stroke-color': ['*', ['get', 'COLOR'], [220, 220, 220]],
        'stroke-width': 2,
        'stroke-offset': -1,
        'fill-color': ['*', ['get', 'COLOR'], [255, 255, 255, 0.6]]
    }


};

export { scaleLineControl, baseLayer, webglVectorLayer }
