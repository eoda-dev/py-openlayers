# See https://openlayers.org/en/latest/examples/tilejson.html

import openlayers as ol

layer = ol.TileLayer(
    source=ol.TileJSONSource(
        url="https://maps.gnosis.earth/ogcapi/collections/NaturalEarth:raster:HYP_HR_SR_OB_DR/map/tiles/WebMercatorQuad?f=tilejson"
    )
)

m = ol.Map(layers=[layer])
m.save()
