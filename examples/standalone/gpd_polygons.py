import openlayers as ol
from openlayers.basemaps import BasemapLayer
from openlayers.colors import Color
from openlayers.styles import FlatStyle

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

# countries = ol.WebGLVectorLayer(source=ol.VectorSource(url=url))
gdf = ol.GeoDataFrame.from_file(url)
gdf["color"] = Color.random_hex_colors_by_category(gdf["name"])
m = gdf.ol.explore(style=FlatStyle(fill_color=["get", "color"], stroke_width=2, stroke_color="red"))
# m.add_layer_call("geopandas", "setOpacity", 0.4)
m.set_opacity("geopandas", 0.5)
# m.set_visible("geopandas", False)
m.save()
