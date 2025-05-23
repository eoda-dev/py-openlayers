import openlayers as ol

data = "https://openlayers.org/en/latest/examples/data/topojson/fr-departments.json"

topojson_layer = ol.VectorLayer(
    source=ol.VectorSource(url=data, format=ol.formats.TopoJSON()),
    style=ol.FlatStyle(
        fill_color="rgba(255,210,120,0.5)",
        stroke_color="green",
        stroke_width=3,
        circle_radius=5,
    ),
    fit_bounds=True,
)

m = ol.Map()
m.add_layer(topojson_layer)
m.add_tooltip()
m.save("/tmp/ol-example.html")
