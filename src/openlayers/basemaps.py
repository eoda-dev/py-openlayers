from .json_defs import OSM, TileLayer


class Basemaps(object):
    OSM = [TileLayer(id="osm", source=OSM())]
