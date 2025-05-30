import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data/gpx/fells_loop.gpx"

gpx_layer = ol.WebGLVectorLayer(
    fit_bounds=True,
    source=ol.VectorSource(url=data, format=ol.formats.GPX()),
    style=ol.FlatStyle(
        circle_fill_color="red", stroke_color="green", stroke_width=3, circle_radius=5
    ),
)

m = ol.Map()
m.add_layer(gpx_layer)
m.add_tooltip()
# m.add_call("addClickInteraction")
m.add_click_interaction()
m.save("/tmp/ol-example.html")
