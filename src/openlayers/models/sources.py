from typing import Union

from pydantic import Field

from .core import OLBaseModel
from .formats import FormatT, GeoJSON


# --- Base source
class Source(OLBaseModel): ...


# --- Sources
class VectorSource(Source):
    """Vector source"""

    url: str | None = None
    # features: list[dict] | None = None
    geojson: dict | None = Field(None, serialization_alias="@@geojson")
    format: FormatT | dict = GeoJSON()


class OSM(Source):
    """OSM source"""

    ...


class GeoTIFFSource(Source):
    """GeoTIFF source"""

    normalize: bool | None = None
    sources: list[dict]


class ImageTileSource(Source):
    """Image tile source"""

    url: str
    attributions: str | None = None
    min_zoom: float | int | None = Field(0, serialization_alias="minZoom")
    max_zoom: float | int | None = Field(20, serialization_alias="maxZoom")


class VectorTileSource(ImageTileSource):
    """A source for vector data divided into a tile grid

    Note:
        See [VectorTile](https://openlayers.org/en/latest/apidoc/module-ol_source_VectorTile-VectorTile.html)
    """

    ...


class TileJSONSource(ImageTileSource):
    """A source for tile data in TileJSON format

    Note:
        See [TileJSON](https://openlayers.org/en/latest/apidoc/module-ol_source_TileJSON-TileJSON.html) for details.
    """

    cross_origin: str = Field("anonymous", serialization_alias="crossOrigin")

    @property
    def type(self) -> str:
        return "TileJSON"


# PMTiles extension
# See https://docs.protomaps.com/pmtiles/openlayers
class PMTilesVectorSource(Source):
    url: str
    attributions: list[str] = None


class PMTilesRasterSource(PMTilesVectorSource):
    tile_size: tuple[int, int] = Field(None, serialization_alias="tileSize")


# --- Source type
SourceT = Union[
    OSM,
    VectorSource,
    GeoTIFFSource,
    ImageTileSource,
    ImageTileSource,
    TileJSONSource,
    PMTilesVectorSource,
    PMTilesRasterSource,
]
