import openlayers as ol

initial_view = ol.View(center=(9.5, 51.31667), zoom=14)

m = ol.Map(initial_view)

# Change view settings afterwards
m.set_center(lon=172.606201, lat=-43.556510)
m.set_zoom(14)

m.set_view(ol.View(center=(172.606201, -43.556510), zoom=12))
