# See https://openlayers.org/en/latest/examples/data/kml/2012-02-10.kml
import openlayers as ol

from openlayers.models.formats import KML
from openlayers.utils import crs_transformer

url = "https://openlayers.org/en/latest/examples/data/kml/2012-02-10.kml"

layer = ol.VectorLayer(
    source=ol.VectorSource(url=url,format=KML())
)

center = crs_transformer().transform(876970.8463461736, 5859807.853963373)

m = ol.Map(ol.View(center=center, zoom=10))
m.add_layer(layer)
m.add_tooltip()
m.save()
