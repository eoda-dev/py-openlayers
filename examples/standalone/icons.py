import openlayers as ol
from openlayers.styles import FlatStyle
from openlayers.basemaps import BasemapLayer
from openlayers.utils import create_icon_src_from_file

url="https://openlayers.org/data/vector/populated-places.json"

style = FlatStyle(
    # icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    icon_src=create_icon_src_from_file("notebooks/data/icon.png"),
    icon_color="steelblue",
    icon_opacity=0.7
    )

icon_layer = ol.VectorLayer(style=style, source=ol.VectorSource(url=url))

m = ol.Map(layers=[BasemapLayer.carto(), icon_layer])
# m.add_tooltip()
m.add_control(ol.controls.OverviewMapControl())
m.save()
