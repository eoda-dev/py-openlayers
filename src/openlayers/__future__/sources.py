from ..models.sources import VectorSource


class GeoJSONSource(VectorSource):
    @property
    def type(self) -> str:
        return "VectorSource"
