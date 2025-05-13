import openlayers as ol

geojson = "https://openlayers.org/en/latest/examples/data/geojson/roads-seoul.geojson"
geotiff = "https://s2downloads.eox.at/demo/EOxCloudless/2020/rgbnir/s2cloudless2020-16bits_sinlge-file_z0-4.tif"
pmtiles = "https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles"

geojson_source = ol.VectorSource(
    url=geojson
)

geotiff_source = ol.GeoTIFFSource(
    sources=[{"url": geotiff}]
)

pmtiles_source = ol.PMTilesVectorSource(
    url=pmtiles,
    attributions=["© Land Information New Zealand"]
)
