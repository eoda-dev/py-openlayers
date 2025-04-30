from .models.sources import OSM
from .models.layers import TileLayer


class Basemaps(object):
    OSM = [TileLayer(id="osm", source=OSM())]
