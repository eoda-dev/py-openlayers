import openlayers as ol
from openlayers.models.sources import PMTilesRasterSource

url = "https://r2-public.protomaps.com/protomaps-sample-datasets/terrarium_z9.pmtiles"

pmtiles = ol.WebGLTileLayer(
    id="pmtiles-raster",
    source=PMTilesRasterSource(
        url=url,
        attributions=[
            "https://github.com/tilezen/joerd/blob/master/docs/attribution.md"
        ],
        tile_size=[512, 512],
    ),
)

view = ol.View(center=(0, 0), zoom=1)

m = ol.Map(view=view, layers=[pmtiles])
m.save()
