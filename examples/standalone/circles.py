import requests as req
import geopandas as gpd
import openlayers as ol
from openlayers.view import Projection

url = "https://openlayers.org/data/vector/populated-places.json"
features = req.get(url).json()

style = {
    "circle-stroke-color": "hsl(0 100% 100% / 0.9)",
    "circle-stroke-width": 0.75,
    "circle-radius": [
        "interpolate",
        ["linear"],
        ["get", "pop_max"],
        500_000,
        3,
        10_000_000,
        10,
    ],
    "circle-fill-color": [
        "interpolate",
        ["linear"],
        ["get", "pop_max"],
        1_000_000,
        "hsl(210 100% 40% / 0.9)",
        10_000_000,
        "hsl(0 80% 60% / 0.9)",
    ],
}

gdf = gpd.GeoDataFrame.from_features(features, crs=Projection.MERCATOR)
m = gdf.ol.explore(style=style, controls=[ol.controls.OverviewMapControl()])
m.save(preview=True)
