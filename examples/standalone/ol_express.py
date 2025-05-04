import json
import openlayers as ol
import openlayers.express as olx

icon_layer = olx.IconLayer(
    id="icon-layer",
    icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    url="https://openlayers.org/data/vector/populated-places.json",
    )
# print(icon_layer.model.model_dump())

polygon_layer = olx.PolygonLayer(
    url="https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson",
    fill_color="steelblue",
    stroke_width=3
    )

m = ol.Map(layers=[polygon_layer, icon_layer])
m.add_tooltip()
# m = ol.Map()
# m.add_layer(icon_layer)

# print(json.dumps(m.calls))
# print(json.dumps(m.map_options))

m.save()
