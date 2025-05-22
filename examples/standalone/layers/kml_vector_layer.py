import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data//kml/states.kml"

kml_layer = ol.VectorLayer(
    source=ol.VectorSource(url=data, format=ol.formats.KML()),
    # style=ol.FlatStyle(fill_color="rgba(255,210,120,0.5)", stroke_color="green", stroke_width=3, circle_radius=5)
)

m = ol.Map()
m.add_layer(kml_layer)
# m.add_tooltip()
# m.add_call("addDragAndDropVectorLayers")
m.add_drag_and_drop_interaction(
    formats=[ol.formats.KML(extract_styles=False)],
    style=ol.FlatStyle(
        stroke_color="red", stroke_width=3, circle_radius=5, circle_stroke_color="green"
    ),
)
m.save("/tmp/ol-example.html")
