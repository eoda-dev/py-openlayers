import openlayers as ol
from openlayers.basemaps import Carto

m = ol.Map(layers=[ol.BasemapLayer(Carto.DARK_ALL)])
m.save()
