geojson_object = {
    "type": "FeatureCollection",
    "crs": {
        "type": "name",
        "properties": {
            "name": "EPSG:3857",
        },
    },
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [0, 0],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [4e6, -2e6],
                    [8e6, 2e6],
                ],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [4e6, 2e6],
                    [8e6, -2e6],
                ],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-5e6, -1e6],
                        [-3e6, -1e6],
                        [-4e6, 1e6],
                        [-5e6, -1e6],
                    ],
                ],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "MultiLineString",
                "coordinates": [
                    [
                        [-1e6, -7.5e5],
                        [-1e6, 7.5e5],
                    ],
                    [
                        [1e6, -7.5e5],
                        [1e6, 7.5e5],
                    ],
                    [
                        [-7.5e5, -1e6],
                        [7.5e5, -1e6],
                    ],
                    [
                        [-7.5e5, 1e6],
                        [7.5e5, 1e6],
                    ],
                ],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [-5e6, 6e6],
                            [-3e6, 6e6],
                            [-3e6, 8e6],
                            [-5e6, 8e6],
                            [-5e6, 6e6],
                        ],
                    ],
                    [
                        [
                            [-2e6, 6e6],
                            [0, 6e6],
                            [0, 8e6],
                            [-2e6, 8e6],
                            [-2e6, 6e6],
                        ],
                    ],
                    [
                        [
                            [1e6, 6e6],
                            [3e6, 6e6],
                            [3e6, 8e6],
                            [1e6, 8e6],
                            [1e6, 6e6],
                        ],
                    ],
                ],
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "GeometryCollection",
                "geometries": [
                    {
                        "type": "LineString",
                        "coordinates": [
                            [-5e6, -5e6],
                            [0, -5e6],
                        ],
                    },
                    {
                        "type": "Point",
                        "coordinates": [4e6, -5e6],
                    },
                    {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [1e6, -6e6],
                                [3e6, -6e6],
                                [2e6, -4e6],
                                [1e6, -6e6],
                            ],
                        ],
                    },
                ],
            },
        },
    ],
}
