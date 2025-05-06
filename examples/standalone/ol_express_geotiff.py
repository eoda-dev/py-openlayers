import openlayers.express as ox

url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/36/Q/WD/2020/7/S2A_36QWD_20200701_0_L2A/TCI.tif"

m = ox.GeoTIFFTileLayer(url=url, opacity=0.7).to_map()
print(m.options)
m.save()
