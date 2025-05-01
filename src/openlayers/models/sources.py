from typing import Union

from pydantic import Field

from .core import OLBaseModel
from .formats import GeoJSON

from ..constants import CARTO_ATTRIBUTION

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

# See also https://github.com/CartoDB/basemap-styles
class ImageTileSource(Source):
    # url: str = "https://{a-d}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}@2x.png"
    # attributions: str | None = CARTO_ATTRIBUTION
    url: str
    attributions: str | None = None
    min_zoom: float | int | None = Field(0, serialization_alias="minZoom")
    max_zoom: float | int | None = Field(20, serialization_alias="maxZoom")


# --- Source type
SourceT = Union[OSM, VectorSource, GeoTIFFSource, ImageTileSource]
