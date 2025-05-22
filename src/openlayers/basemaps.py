from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from .abstracts import LayerLike
from .models.layers import TileLayer
from .models.sources import OSM, ImageTileSource

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
    VOYAGER_NO_LABLES = "rastertiles/voyager_nolabels"


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
    def __init__(self, style_name: Carto | str = Carto.DARK_ALL):
        self._model = BasemapLayer.carto(style_name)

    @property
    def model(self) -> TileLayer:
        return self._model
