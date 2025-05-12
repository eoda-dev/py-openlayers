from __future__ import annotations

from typing import Literal, Union
from uuid import uuid4

from pydantic import Field, field_validator

from .core import OLBaseModel
from .layers import LayerT, TileLayer
from .sources import OSM


# -- Base control
class Control(OLBaseModel):
    id: str | None = None  # = Field(default_factory=lambda x: str(uuid4()))

    @field_validator("id")
    def validate_id(cls, v) -> str:
        if v is None:
            return uuid4().hex[0:10]

        return v


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


class ZoomControl(Control):
    zoom_in_label: str = Field("+", serialization_alias="zoomInLabel")
    zoom_out_label: str = Field("-", serialization_alias="zoomOutLabel")


class RotateControl(Control): ...


# --- Custom controls
class InfoBox(Control):
    html: str
    css_text: str = Field(
        "top: 65px; left: .5em; padding: 5px;", serialization_alias="cssText"
    )

class DrawControl(Control): ...


# --- Control type
ControlT = Union[
    Control,
    FullScreenControl,
    ScaleLineControl,
    ZoomSliderControl,
    OverviewMapControl,
    ZoomControl,
    RotateControl,
    InfoBox,
    DrawControl
]
