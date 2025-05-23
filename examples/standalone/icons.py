import openlayers as ol
from openlayers.styles import FlatStyle, IconStyle
from openlayers.basemaps import BasemapLayer
from openlayers.utils import create_icon_src_from_file

url="https://openlayers.org/data/vector/populated-places.json"

icon = "https://maplibre.org/maplibre-gl-js/docs/assets/osgeo-logo.png"
# icon = "https://upload.wikimedia.org/wikipedia/commons/7/7c/201408_cat.png"

style = IconStyle(
    # icon_src="https://openlayers.org/en/latest/examples/data/icon.png",
    # icon_src=create_icon_src_from_file("notebooks/data/icon.png"),
    icon_src=icon,
    # icon_color="steelblue",
    # icon_opacity=0.7,
    # icon_scale=0.2
    )

icon_style = FlatStyle(
    icon_src="https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png",
    icon_color="green",
    icon_width=64,
    icon_height=64,
    # icon_anchor_x_units="pixels",
    # icon_anchor_y_units="pixels",
    # icon_anchor=[128, 0]
    icon_offset=[128, 0],
    icon_size=[128, 128]
)
print(icon_style.model_dump())

icon_layer = ol.VectorLayer(style=style, source=ol.VectorSource(url=url))

m = ol.Map(layers=[BasemapLayer.carto(), icon_layer])
m.add_tooltip()
m.add_control(ol.controls.OverviewMapControl())
print(m.options)
m.save()
