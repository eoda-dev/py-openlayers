import openlayers.express as ox

url = "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/36/Q/WD/2020/7/S2A_36QWD_20200701_0_L2A/TCI.tif"
url = "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
url = "https://maplibre.org/maplibre-gl-js/docs/assets/cog.tif"

m = ox.GeoTIFFTileLayer(url=url, opacity=0.7).to_map(layers=[])
print(m.options)
print(m.calls)
m.save()
