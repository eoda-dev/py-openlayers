import openlayers as ol
from openlayers.geopandas import GeoDataFrame

data = "https://openlayers.org/en/latest/examples/data/geojson/roads-seoul.geojson"

m = GeoDataFrame.from_file(data).ol.explore(tooltip=True)
m.add_control(ol.ScaleLineControl())
