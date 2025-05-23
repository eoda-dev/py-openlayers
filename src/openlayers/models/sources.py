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
    """GeoTIFF source

    Examples:
        >>> import ol
        >>> geotiff = ol.GeoTIFFSource(sources=[{"url": "https://s2downloads.eox.at/demo/EOxCloudless/2020/rgbnir/s2cloudless2020-16bits_sinlge-file_z0-4.tif"}])
    """

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
        See [VectorTile](https://openlayers.org/en/latest/apidoc/module-ol_source_VectorTile-VectorTile.html) for details.
    """

    ...


class TileJSONSource(ImageTileSource):
    """A source for tile data in TileJSON format

    Note:
        See [TileJSON](https://openlayers.org/en/latest/apidoc/module-ol_source_TileJSON-TileJSON.html) for details.
    """

    tile_size: int | None = Field(None, serialization_alias="tileSize")
    cross_origin: str = Field("anonymous", serialization_alias="crossOrigin")

    @property
    def type(self) -> str:
        return "TileJSON"


# PMTiles extension
# See https://docs.protomaps.com/pmtiles/openlayers
class PMTilesVectorSource(Source):
    """PMTiles vector source"""

    url: str
    attributions: list[str] = None


class PMTilesRasterSource(PMTilesVectorSource):
    """PMTiles raster source"""

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
