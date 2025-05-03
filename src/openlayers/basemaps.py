from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

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


class BasemapLayer(object):
    @staticmethod
    def osm() -> TileLayer:
        return TileLayer(id="osm", source=OSM())

    @staticmethod
    def carto(
        style_name: str | Carto = Carto.DARK_ALL, double_resolution: bool = True
    ) -> TileLayer:
        style = CartoRasterStyle(style=style_name, double_resolution=double_resolution)
        return TileLayer(
            id=f"carto-{Carto(style_name).value.replace('_', '-')}",
            source=ImageTileSource(url=style.url, attributions=style.attribution),
        )


"""
 new OGCMapTile({
    url: 'https://maps.gnosis.earth/ogcapi/collections/NaturalEarth:raster:HYP_HR_SR_OB_DR/map/tiles/WebMercatorQuad',
    crossOrigin: '',
  }),
"""
