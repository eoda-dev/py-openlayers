# See https://openlayers.org/en/latest/examples/data/kml/2012-02-10.kml
import openlayers as ol

from openlayers.models.formats import KML
from openlayers.utils import crs_transformer

url = "https://openlayers.org/en/latest/examples/data/kml/2012-02-10.kml"
center = crs_transformer().transform(876970.8463461736, 5859807.853963373)

url ="https://openlayers.org/en/latest/examples/data/kml/2012_Earthquakes_Mag5.kml"

layer = ol.VectorLayer(
    style=ol.FlatStyle(circle_fill_color="green", circle_radius=7),
    source=ol.VectorSource(url=url,format=KML(extract_styles=False))
)


# m = ol.Map(ol.View(center=center, zoom=10))
m = ol.Map()
m.add_layer(layer)
m.add_tooltip()
m.save()
