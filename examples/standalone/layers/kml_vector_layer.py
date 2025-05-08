import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data//kml/states.kml"

kml_layer = ol.VectorLayer(
    source=ol.VectorSource(
        url=data,
        format=ol.formats.KML()
    ),
    # style=ol.FlatStyle(fill_color="rgba(255,210,120,0.5)", stroke_color="green", stroke_width=3, circle_radius=5)
)

m = ol.Map()
m.add_layer(kml_layer)
m.add_tooltip()
m.save("/tmp/ol-example.html")
