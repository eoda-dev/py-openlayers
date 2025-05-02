import openlayers as ol
from openlayers.styles import default_style

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

# layer = ol.WebGLTileLayer(source=ol.VectorSource(url=""))
layer = ol.WebGLVectorLayer(source=ol.VectorSource(url=url), style=default_style())

m = ol.Map(layers=[layer])
m.add_tooltip("name")
m.add_control(ol.controls.ZoomSliderControl())
m.save()
