import openlayers as ol
from openlayers.basemaps import MapTilerBasemapLayer, MapTiler, CartoBasemapLayer, Carto

m = ol.Map()
m.set_zoom(2)
# m.add_layer(MapTilerBasemapLayer(MapTiler.TONER))
m.add_layer(CartoBasemapLayer(Carto.VOYAGER_LABELS_UNDER))
m.add_control(ol.MapTilerGeocodingControl())
m.save()
