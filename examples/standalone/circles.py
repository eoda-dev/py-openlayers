import requests as req
import geopandas as gpd
import openlayers as ol
from openlayers.view import Projection

url = "https://openlayers.org/data/vector/populated-places.json"
features = req.get(url).json()

gdf = gpd.GeoDataFrame.from_features(features, crs=Projection.MERCATOR)
m = gdf.ol.explore()
m.save(preview=True)
