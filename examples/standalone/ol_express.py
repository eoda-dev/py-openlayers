import json
import openlayers as ol
import openlayers.express as olx

icon_layer = olx.IconLayer(
    id="icon-layer",
    icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    url="https://openlayers.org/data/vector/populated-places.json",
    )
# print(icon_layer.model.model_dump())

m = ol.Map(layers=[icon_layer])

# m = ol.Map()
# m.add_layer(icon_layer)

# print(json.dumps(m.calls))
# print(json.dumps(m.map_options))

m.save()
