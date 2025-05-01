import openlayers as ol
# from openlayers.anywidget import MapWidget
# from openlayers.map import Map

layer = ol.WebGLTileLayer(source=ol.VectorSource(url=""))

m = ol.Map(layers=[layer])
m.save()
