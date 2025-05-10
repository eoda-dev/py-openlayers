from typing import Union

from pydantic import Field

from .core import OLBaseModel
from .formats import FormatT, GeoJSON

# from ..constants import CARTO_ATTRIBUTION


# --- Base source
class Source(OLBaseModel): ...


# --- Sources
class VectorSource(Source):
    url: str | None = None
    # features: list[dict] | None = None
    geojson: dict | None = Field(None, serialization_alias="@@geojson")
    format: FormatT | dict = GeoJSON()


class OSM(Source): ...


class GeoTIFFSource(Source):
    normalize: bool | None = None
    sources: list[dict]


class ImageTileSource(Source):
    url: str
    attributions: str | None = None
    min_zoom: float | int | None = Field(0, serialization_alias="minZoom")
    max_zoom: float | int | None = Field(20, serialization_alias="maxZoom")


"""
const vectorLayer = new VectorTile({
  declutter: true,
  source: new PMTilesVectorSource({
    url: "https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles",
    attributions: ["© Land Information New Zealand"],
  }),
"""

# PMTiles extension
# See https://docs.protomaps.com/pmtiles/openlayers
class PMTilesVectorSource(Source):
    url: str
    attributions: list[str] = None


class PMTilesRasterSource(PMTilesVectorSource):
    tile_size: tuple[int, int] = Field(None, serialization_alias="tileSize")


# --- Source type
SourceT = Union[OSM, VectorSource, GeoTIFFSource, ImageTileSource, PMTilesVectorSource, PMTilesRasterSource]
