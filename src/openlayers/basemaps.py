from .models.sources import OSM
from .models.layers import TileLayer


class Basemaps(object):
    OSM = [TileLayer(id="osm", source=OSM())]

"""
 new OGCMapTile({
    url: 'https://maps.gnosis.earth/ogcapi/collections/NaturalEarth:raster:HYP_HR_SR_OB_DR/map/tiles/WebMercatorQuad',
    crossOrigin: '',
  }),
"""