import openlayers as ol

geojson = ol.VectorSource(
    url="https://openlayers.org/en/latest/examples/data/geojson/roads-seoul.geojson"
)

geotiff = ol.GeoTIFFSource(
    sources=[{"url": "https://s2downloads.eox.at/demo/EOxCloudless/2020/rgbnir/s2cloudless2020-16bits_sinlge-file_z0-4.tif"}]
)

pmtiles = ol.PMTilesVectorSource(
    url="https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles",
    attributions=["© Land Information New Zealand"]
)
