from __future__ import annotations

from pydantic import Field

# from ..abstracts import MyBaseModel
from .core import OLBaseModel


# TODO: Use pyproj instead
class Projection(object):
    MERCATOR = "EPSG:4326"
    WEB_MERCATOR = "EPSG:3857"

    @staticmethod
    def from_epsg(code: int) -> str:
        return f"EPSG:{code}"


# TODO: Obsolete, remove
"""
class ViewOptions(MyBaseModel):
    center: tuple[float, float] | None = (0, 0)
    zoom: float | None = 0
    projection: str | None = Projection.WEB_MERCATOR
    min_zoom: int | float | None = None
    max_zoom: int | float | None = None
"""


class View(OLBaseModel):
    """View object

    Note:
        See [module-ol_View-View.html](https://openlayers.org/en/latest/apidoc/module-ol_View-View.html) for details.

    Attributes:
        center (tuple[float, float]): The centerpoint of the map as `(lon, lat)` pair
        zoom (float | int): The zoom level of the map
        extent (tuple[float, float, float, float] | list[float, float, float, float]): ...
        min_zoom (float | int): The minimum zoom level of the map
        max_zoom (float | int): The maximum zoom level of the map
    """

    center: tuple[float, float] | None = (0, 0)
    zoom: float | int | None = 0
    projection: str | None = Projection.WEB_MERCATOR
    extent: (
        tuple[float, float, float, float] | list[float, float, float, float] | None
    ) = None
    min_zoom: int | float | None = Field(None, serialization_alias="minZoom")
    max_zoom: int | float | None = Field(None, serialization_alias="maxZoom")
