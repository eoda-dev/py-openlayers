import openlayers as ol

data = "zip+https://github.com/Toblerity/Fiona/files/11151652/coutwildrnp.zip"

gdf = ol.GeoDataFrame.from_file(data)
print(gdf.crs)

# print(gdf)
m = gdf.ol.color_category("STATE").explore()
# m.add_call("fitBoundsFromLonLat", list(gdf.total_bounds))
# m.fit_bounds(list(gdf.total_bounds))
# m.set_view(ol.View(extent=list(gdf.total_bounds)))
m.save()
