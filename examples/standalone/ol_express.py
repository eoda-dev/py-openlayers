# import json
# import openlayers as ol
import openlayers.express as ox
from openlayers.basemaps import BasemapLayer
from openlayers import View

icon_layer = ox.IconLayer(
    # id="icon-layer",
    data="https://openlayers.org/data/vector/populated-places.json",
    icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    )
# print(icon_layer.model.model_dump())

"""
polygon_layer = olx.PolygonLayer(
    url="https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson",
    fill_color="steelblue",
    stroke_width=3
    )
"""

line_data = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart.geo.json"

generic_geojson_layer = ox.GeoJSONLayer(
    data = line_data,
    #stroke_width = 5,
    #stroke_color = "green",
    #circle_fill_color = "red",
    #circle_stroke_color = "steelblue",
    #circle_stroke_width = 3,
    #circle_radius = 7
)

circle_layer = ox.CircleLayer(
    data="https://openlayers.org/data/vector/populated-places.json",
    circle_fill_color="yellow"
    )

fill_layer = ox.FillLayer(
    data=None ,#"https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson",
    stroke_width=4,
    fill_color="yellow",
    id="fill"
    )
# m = fill_layer.to_map()
m = generic_geojson_layer.to_map(lon=-122.4, lat=37.74, zoom=11, layers=[BasemapLayer.carto()])
# m.add_call("setExtentFromSource", "fill")
# m = circle_layer.to_map()
# m = ol.Map(layers=[fill_layer, circle_layer])
m.add_tooltip()
# m = ol.Map()
# m.add_layer(icon_layer)

# print(json.dumps(m.calls))
# print(json.dumps(m.map_options))

# m.set_center((9.5, 51.31667))
# m.set_view(View(center=(9.5, 51.31667), zoom=14))
m.save()
