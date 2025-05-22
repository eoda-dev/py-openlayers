from __future__ import annotations

import os

from enum import Enum

from pydantic import BaseModel, Field

from .abstracts import LayerLike
from .models.layers import TileLayer
from .models.sources import OSM, ImageTileSource, TileJSONSource
from .constants import MAPTILER_API_KEY_ENV_VAR

# light_all,
# dark_all,
# light_nolabels,
# light_only_labels,
# dark_nolabels,
# dark_only_labels,
# rastertiles/voyager,
# rastertiles/voyager_nolabels,
# rastertiles/voyager_only_labels,
# rastertiles/voyager_labels_under


class Carto(Enum):
    """CartoDB basemap styles"""

    LIGHT_ALL = "light_all"
    DARK_ALL = "dark_all"
    LIGHT_NO_LABELS = "light_nolabels"
    LIGHT_ONLY_LABELS = "light_only_labels"
    DARK_NO_LABELS = "dark_nolabels"
    DARK_ONLY_LABELS = "dark_only_labels"
    VOYAGER = "rastertiles/voyager"
    VOYAGER_NO_LABELS = "rastertiles/voyager_nolabels"
    VOYAGER_ONLY_LABELS = "rastertiles/voyager_only_labels"
    VOYAGER_LABELS_UNDER = "rastertiles/voyager_labels_under"


class CartoRasterStyle(BaseModel):
    style: Carto | str = Carto.DARK_ALL
    double_resolution: bool = False

    @property
    def attribution(self) -> str:
        return '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attributions">CARTO</a>'

    @property
    def url(self) -> str:
        resolution = "@2x" if self.double_resolution else ""
        return (
            "https://{a-d}.basemaps.cartocdn.com/"
            + Carto(self.style).value
            + "/{z}/{x}/{y}"
            + resolution
            + ".png"
        )


class BasemapLayer(LayerLike):
    def __init__(self, style: str | Carto = None) -> None:
        if isinstance(style, Carto):
            self._model = BasemapLayer.carto(style)
        else:
            self._model = BasemapLayer.osm()

    @property
    def model(self) -> TileLayer:
        return self._model

    @staticmethod
    def osm() -> TileLayer:
        """Create a OSM tile layer object

        Returns:
            An OSM raster tile layer

        Examples:
            >>> from openlayers.basemaps import BasemapLayer
            >>> osm = BasemapLayer.osm()
        """
        return TileLayer(id="osm", source=OSM())

    @staticmethod
    def carto(
        style_name: str | Carto = Carto.DARK_ALL, double_resolution: bool = True
    ) -> TileLayer:
        """Create a CartoDB tile layer object

        Note:
            See [CartoDB/basemap-styles](https://github.com/CartoDB/basemap-styles) for available styles.

        Args:
            style_name (str | Carto): The name of the style
            double_resolution (bool): Whether to use double resolution tiles

        Returns:
            A CartoDB raster tile layer

        Examples:
            >>> from openlayers.basemaps import BasemapLayer
            >>> carto = BasemapLayer.carto()
        """
        style = CartoRasterStyle(style=style_name, double_resolution=double_resolution)
        return TileLayer(
            id=f"carto-{Carto(style_name).value.replace('_', '-').replace('/', '-')}",
            source=ImageTileSource(url=style.url, attributions=style.attribution),
        )


"""
 new OGCMapTile({
    url: 'https://maps.gnosis.earth/ogcapi/collections/NaturalEarth:raster:HYP_HR_SR_OB_DR/map/tiles/WebMercatorQuad',
    crossOrigin: '',
  }),
"""


class CartoBasemapLayer(LayerLike):
    def __init__(
        self, style_name: Carto | str = Carto.DARK_ALL, double_resolution: bool = True
    ):
        style = CartoRasterStyle(style=style_name, double_resolution=double_resolution)
        self._model = TileLayer(
            id=f"carto-{Carto(style_name).value.replace('_', '-').replace('/', '-')}",
            source=ImageTileSource(url=style.url, attributions=style.attribution),
        )

    @property
    def model(self) -> TileLayer:
        return self._model


class MapTiler(Enum):
    BASIC_V2 = "basic-v2"
    STREETS_V2 = "streets-v2"
    HYBRID = "hybrid"
    DATAVIZ_DARK = "dataviz-dark"

    AQUARELLE = "aquarelle"
    BACKDROP = "backdrop"
    BASIC = "basic"
    BRIGHT = "bright"
    DATAVIZ = "dataviz"
    LANDSCAPE = "landscape"
    OCEAN = "ocean"
    OPEN_STREET_MAP = "openstreetmap"
    OUTDOOR = "outdoor"
    SATELLITE = "satellite"
    STREETS = "streets"
    TONER = "toner"
    TOPO = "topo"
    WINTER = "winter"


class MapTilerValidator(BaseModel):
    api_key: str = Field(os.getenv(MAPTILER_API_KEY_ENV_VAR), validate_default=True)


class MapTilerBasemapLayer(LayerLike):
    def __init__(
        self,
        style_name: MapTiler | str = MapTiler.STREETS_V2,
        api_key: str = os.getenv(MAPTILER_API_KEY_ENV_VAR),
    ) -> None:
        style = (
            MapTiler(style_name).value
            if isinstance(style_name, MapTiler)
            else style_name
        )
        key = MapTilerValidator(api_key=api_key).api_key
        url = f"https://api.maptiler.com/maps/{style}/tiles.json?key={key}"
        self._model = TileLayer(
            id=f"maptiler-{style}",
            source=TileJSONSource(url=url, tile_size=512, cross_origin="anonymous"),
        )

    @property
    def model(self) -> TileLayer:
        return self._model
