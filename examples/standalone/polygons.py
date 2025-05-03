import openlayers as ol
from openlayers.basemaps import BasemapLayer

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

countries = ol.WebGLVectorLayer(source=ol.VectorSource(url=url))

m = ol.Map(layers=[BasemapLayer.carto(), countries])
m.add_tooltip("{{ name }}")
# m.add_tooltip()
m.add_control(ol.controls.ZoomSliderControl())
m.add_control(ol.controls.InfoBox(
    html="OpenLayers4Py",
    css_text="right: .5em; top: .5em; background: white; padding: 5px;"))
m.save()
