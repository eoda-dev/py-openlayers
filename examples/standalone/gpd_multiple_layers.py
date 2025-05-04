import openlayers as ol
from openlayers.basemaps import BasemapLayer
from openlayers.styles import FlatStyle

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

style = FlatStyle(fill_color="green", stroke_color="steelblue")

gpd = ol.GeoDataFrame.from_file(url)

# countries_layer = gpd.ol.to_layer(style=style, opacity=0.5)
countries_layer = gpd.ol.color_category("name").to_layer(opacity=0.5)

m = ol.Map(layers=[BasemapLayer.carto(), countries_layer])
m.save()
