import openlayers as ol
from openlayers.basemaps import MapTilerBasemapLayer, MapTiler, CartoBasemapLayer, Carto

m = ol.Map(layers=[])
m.set_zoom(2)
m.add_layer(ol.BasemapLayer())
# m.add_layer(MapTilerBasemapLayer(MapTiler.AQUARELLE))
# m.add_layer(CartoBasemapLayer(Carto.VOYAGER_LABELS_UNDER))
m.add_control(ol.MapTilerGeocodingControl(country="de"))
m.save()
