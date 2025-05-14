import openlayers as ol
import openlayers.express as ox

data = "https://openlayers.org/data/vector/populated-places.json"

m = ox.Vector(
    data, fit_bounds=False, style=ox.default_style(circle_fill_color="red")
).explore()
# m.save()

m = ox.Vector(
    data="https://openlayers.org/en/latest/examples/data//kml/states.kml",
    # style=None,
    webgl=True
    # data="https://openlayers.org/en/latest/examples/data/gpx/fells_loop.gpx"
).explore()
m.save()
