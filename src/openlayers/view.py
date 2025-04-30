from.models.view import View, Projection

class CRS(object):
    MERCATOR = "EPSG:3857"
    EPSG_3857 = "EPSG:3857"
    WGS_84 = "EPSG:4326"
    EPSG_4326 = "EPSG:4326"

__all__ = ["Projection", "View"]
