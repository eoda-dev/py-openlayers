import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data/geojson/roads-seoul.geojson"

geojson_layer = ol.VectorLayer(
    id="roads",
    source=ol.VectorSource(url=data, format=ol.formats.GeoJSON()),
    style=ol.FlatStyle(
        fill_color="rgba(255,210,120,0.5)",
        stroke_color="green",
        stroke_width=3,
        circle_radius=5,
    ),
    fit_bounds=True,
)

zoom_slider = ol.ZoomSliderControl()

m = ol.Map(ol.View(rotation=3.14 / 8), layers=[ol.BasemapLayer.carto()])
m.add_control(zoom_slider)
m.add_layer(geojson_layer)
m.add_tooltip()
m.add_control(ol.DrawControl())
# m.remove_control(zoom_slider.id)
# m.add_call("addModifyInteraction", geojson_layer.id)
# m.add_modify_interaction(geojson_layer.id)
m.save("/tmp/ol-example.html")
