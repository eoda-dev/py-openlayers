from typing import Literal

from .abstracts import BaseType


class Control(BaseType): ...


class FullScreenControl(Control): ...


class ScaleLineControl(Control):
    bar: bool = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False


class ZoomSliderControl(Control): ...


class MousePositionControl(Control):
    projection: str | None = "EPSG:4326"


# TODO: Needs JS for parsing of layers
"""
class OverviewMapControl(Control):
    layers: list[dict]
"""
