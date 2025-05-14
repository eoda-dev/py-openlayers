# See https://openlayers.org/en/latest/examples/cog-overviews.html
import openlayers as ol

layer = ol.WebGLTileLayer(
    source=ol.GeoTIFFSource(
        sources=[
            dict(
                url="https://openlayers.org/data/raster/no-overviews.tif",
                overviews=["https://openlayers.org/data/raster/no-overviews.tif.ovr"],
            )
        ]
    )
)

m = ol.Map(layers=[layer])
m.set_view_from_source(layer.id)
m.save()
