from pydantic import computed_field

from .abstracts import MyBaseModel, Source


class OSM(Source):
    @computed_field
    def type(self) -> str:
        return "OSM"

class VectorSource(Source):
    url: str = None
    format: str = "GeoJSON"
    
    @computed_field
    def type(self) -> str:
        return "VectorSource"
