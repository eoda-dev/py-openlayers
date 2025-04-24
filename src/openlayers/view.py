from __future__ import annotations

from .abstracts import MyBaseModel


class Projection:
    EPSG_4326 = "EPSG:4326"


class View(MyBaseModel):
    center: tuple[float, float] | None = (0, 0)
    zoom: float | None = 0
    projection: str | None = None
    min_zoom: int | float | None = None
    max_zoom: int | float | None = None
