import openlayers as ol
from openlayers.basemaps import CartoBasemapLayer, Carto

# Use default OSM basemap
m = ol.Map(layers=[ol.BasemapLayer()])

# Use a CartoDB basemap
m = ol.Map(layers=[CartoBasemapLayer(Carto.DARK_NO_LABELS)])
