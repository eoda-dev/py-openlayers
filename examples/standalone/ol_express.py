import json
import openlayers as ol
import openlayers.express as olx

icon_layer = olx.IconLayer(
    # id="icon-layer",
    data="https://openlayers.org/data/vector/populated-places.json",
    icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    )
# print(icon_layer.model.model_dump())

polygon_layer = olx.PolygonLayer(
    url="https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson",
    fill_color="steelblue",
    stroke_width=3
    )

circle_layer = olx.CircleLayer(
    data="https://openlayers.org/data/vector/populated-places.json",
    circle_fill_color="yellow"
    )

fill_layer = olx.FillLayer(
    data=None ,#"https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson",
    stroke_width=4,
    fill_color="yellow",
    id="fill"
    )
m = fill_layer.to_map()
m.add_call("setExtentFromSource", "fill")
# m = circle_layer.to_map()
# m = ol.Map(layers=[fill_layer, circle_layer])
m.add_tooltip()
# m = ol.Map()
# m.add_layer(icon_layer)

# print(json.dumps(m.calls))
# print(json.dumps(m.map_options))

m.save()
