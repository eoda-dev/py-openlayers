import openlayers as ol
import openlayers.express as olx

icon_layer = olx.IconLayer(
    icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    url="https://openlayers.org/data/vector/populated-places.json",
    )
print(icon_layer.model_dump())

m = ol.Map(layers=[icon_layer.model_dump()])
m.save()
