import openlayers as ol

# Use OSM basemap
m = ol.Map(layers=[ol.BasemapLayer.osm()])

# Use a CartoDB basemap
m = ol.Map(layers=[ol.BasemapLayer.carto()])
