from __future__ import annotations

from typing import Literal, Union
from uuid import uuid4

from pydantic import Field

from .core import OLBaseModel
from .layers import LayerT, TileLayer
from .sources import OSM


# -- Base control
class Control(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))


# --- Controls
class FullScreenControl(Control): ...


class ScaleLineControl(Control):
    bar: bool | None = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False


class ZoomSliderControl(Control): ...


class MousePositionControl(Control):
    projection: str | None = "EPSG:4326"


class OverviewMapControl(Control):
    layers: list[dict | LayerT] = [TileLayer(source=OSM())]


# --- Custom controls
class InfoBox(Control):
    html: str
    css_text: str = Field(
        "top: 65px; left: .5em; padding: 5px;", serialization_alias="cssText"
    )


# --- Control type
ControlT = Union[
    Control,
    FullScreenControl,
    ScaleLineControl,
    ZoomSliderControl,
    OverviewMapControl,
    InfoBox,
]
