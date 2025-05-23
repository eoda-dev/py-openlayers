import openlayers as ol
from openlayers.basemaps import BasemapLayer

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

countries = ol.WebGLVectorLayer(source=ol.VectorSource(url=url))

m = ol.Map(ol.View(projection="EPSG:4326"), layers=[BasemapLayer.osm(), countries])
m.add_tooltip("{{ name }}")
# m.add_tooltip()
m.remove_control("zoom")
m.add_control(ol.controls.ZoomControl(zoom_in_label="I", zoom_out_label="O"))
m.add_control(ol.controls.ZoomSliderControl())
m.add_control(ol.controls.InfoBox(
    html="PyOL",
    css_text="right: .5em; top: .5em; background: white; padding: 5px;"))
m.add_control(ol.controls.ZoomToExtentControl())
m.save()
