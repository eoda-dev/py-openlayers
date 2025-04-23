from __future__ import annotations

from .abstracts import MyBaseModel


class View(MyBaseModel):
    center: tuple[float, float] | None = (0, 0)
    zoom: float | None = 0
    min_zoom: int | float | None = None
    max_zoom: int | float | None = None
