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

// TODO: '@@type' must always be the first entry!
const populatedPlaces = {

    'source': {
        'url': 'https://openlayers.org/data/vector/populated-places.json',
        'format': {
            '@@type': 'GeoJSON'
        },
        '@@type': 'VectorSource',
    },
    'style': {
        'circle-fill-color': 'red',
        'circle-stroke-color': 'yellow',
        'circle-stroke-width': 0.75,
        'circle-radius': 5
    },
    '@@type': 'WebGLVectorLayer',
}

export { scaleLineControl, baseLayer, webglVectorLayer, populatedPlaces as populatedPlacesLayer }
