# VectorTileLayer: https://unpkg.com/world-atlas@1.1.4/world/50m.json
import openlayers as ol

mvt_layer = ol.layers.VectorTileLayer(
    source=ol.sources.VectorTileSource(
        url='https://basemaps.arcgis.com/arcgis/rest/services/World_Basemap_v2/VectorTileServer/tile/{z}/{y}/{x}.pbf',
        format=ol.formats.MVT()
    )
)

m = ol.Map(layers=[mvt_layer])
m.add_default_tooltip()
m.save()
