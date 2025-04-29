from typing import Union

from pydantic import Field

from .core import OLBaseModel
from .formats import GeoJSON


# --- Base source
class Source(OLBaseModel): ...


# --- Sources
class VectorSource(Source):
    url: str | None = None
    features: list[dict] | None = None
    geojson: dict | None = Field(None, serialization_alias="@@geojson")
    format: dict | GeoJSON = GeoJSON()


class OSM(Source): ...


class GeoTIFFSource(Source):
    normalize: bool | None = None
    sources: list[dict]


# --- Source type
SourceT = Union[OSM, VectorSource, GeoTIFFSource]
