from .json_defs import TileLayer, OSM

class Basemaps(object):
    OSM = [TileLayer(id="osm", source=OSM())]
