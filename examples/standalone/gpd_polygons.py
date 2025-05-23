import openlayers as ol
# from openlayers.basemaps import BasemapLayer

url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"

gdf = ol.GeoDataFrame.from_file(url)
m = gdf.ol.color_category("name").explore(controls=[ol.OverviewMapControl()])

m.set_opacity("geopandas", 0.5)
# m.set_visible("geopandas", False)
m.add_call("addOverlay", (9.5, 51.31667), "Kassel", "background-color: white; padding: 5px; border-radius: 4px;")
m.set_center((9.5, 51.31667))
m.save()
