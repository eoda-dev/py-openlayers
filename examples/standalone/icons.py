import openlayers as ol
from openlayers.styles import VectorStyle

url="https://openlayers.org/data/vector/populated-places.json"

style = VectorStyle().model_dump()

style={
    "icon-src": "https://openlayers.org/en/latest/examples/data/icon.png"
}

layer = ol.VectorLayer(style=style, source=ol.VectorSource(url=url))

m = ol.MapWidget(layers=[layer])
# m.add_tooltip()
m.save()
