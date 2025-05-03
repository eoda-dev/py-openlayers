from __future__ import annotations

from ..abstracts import MyBaseModel
from .core import OLBaseModel


class Projection(object):
    MERCATOR = "EPSG:4326"
    WEB_MERCATOR = "EPSG:3857"

    @staticmethod
    def from_epsg(code: int) -> str:
        return f"EPSG:{code}"


class ViewOptions(MyBaseModel):
    center: tuple[float, float] | None = (0, 0)
    zoom: float | None = 0
    projection: str | None = Projection.WEB_MERCATOR
    min_zoom: int | float | None = None
    max_zoom: int | float | None = None


class View(OLBaseModel):
    center: tuple[float, float] | None = (0, 0)
    zoom: float | None = 0
    projection: str | None = Projection.WEB_MERCATOR
    min_zoom: int | float | None = None
    max_zoom: int | float | None = None
