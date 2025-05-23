# See https://openlayers.org/en/latest/examples/image-vector-layer.html

import openlayers as ol

data = "https://openlayers.org/data/vector/ecoregions.json"

style = ol.FlatStyle(
    fill_color=['string', ['get', 'COLOR'], '#eee']
)

layer = ol.VectorImageLayer(
    background="#1a2b39",
    image_ratio=2,
    source=ol.VectorSource(url=data),
    style=style
)

m = ol.Map(layers=[layer])
m.save()
