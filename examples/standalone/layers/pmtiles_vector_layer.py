import openlayers as ol
from openlayers.models.sources import PMTilesVectorSource
from openlayers.styles import default_style

url = (
    "https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles"
)

pmtiles = ol.layers.VectorTileLayer(
    id="pmtiles-vector",
    style=default_style(stroke_color="green", stroke_width=2),
    source=PMTilesVectorSource(
        url=url, attributions=["© Land Information New Zealand"]
    ),
)

view = ol.View(center=(172.606201, -43.556510), zoom=12)

m = ol.Map(view=view, layers=[pmtiles])
m.add_tooltip()
m.save()
