import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data/geojson/roads-seoul.geojson"

vector = ol.VectorLayer(
    id="roads",
    source=ol.VectorSource(url=data),
    fit_bounds=True,
)


m = ol.Map(
    ol.View(rotation=3.14 / 8),
    layers=[ol.BasemapLayer(), vector]
)
m.add_default_tooltip()
