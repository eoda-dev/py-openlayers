from __future__ import annotations

import os
from typing import Literal, Union
from uuid import uuid4

from pydantic import Field, field_validator

from ..constants import MAPTILER_API_KEY_ENV_VAR
from .core import OLBaseModel
from .layers import LayerT, TileLayer
from .sources import OSM


# -- Base control
class Control(OLBaseModel):
    id: str | None = None

    @field_validator("id")
    def validate_id(cls, v) -> str:
        if v is None:
            return uuid4().hex[0:10]

        return v


# --- Controls
class FullScreenControl(Control):
    """Full screen control

    Provides a button that fills the entire screen with the map when clicked.
    """

    ...


class ScaleLineControl(Control):
    """Scale line control

    Displays rough y-axis distances that are calculated for the centre of the viewport.
    """

    bar: bool | None = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False


class ZoomSliderControl(Control):
    """Zoom slider control"""

    ...


class MousePositionControl(Control):
    """Mouse position control"""

    projection: str | None = "EPSG:4326"


class OverviewMapControl(Control):
    """Overview map control"""

    layers: list[dict | LayerT] = [TileLayer(source=OSM())]


class ZoomControl(Control):
    """Zoom control"""

    zoom_in_label: str = Field("+", serialization_alias="zoomInLabel")
    zoom_out_label: str = Field("-", serialization_alias="zoomOutLabel")


class RotateControl(Control):
    """Rotate control"""

    ...


class ZoomToExtentControl(Control):
    """Zoom to extent control

    Provides a button that changes the map view to a specific extent when clicked.
    """

    extent: (
        tuple[float | float | float | float]
        | list[float | float | float | float]
        | None
    ) = None


# --- MapTiler
class MapTilerGeocodingControl(Control):
    """MapTiler geocoding control"""

    api_key: str = Field(
        os.getenv(MAPTILER_API_KEY_ENV_VAR),
        serialization_alias="apiKey",
        validate_default=True,
    )
    collapsed: bool | None = False
    country: str | None = None
    limit: int | None = 5
    marker_on_selected: bool | None = Field(
        True, serialization_alias="markerOnSelected"
    )
    placeholder: str | None = "Search"


# --- Custom controls
class InfoBox(Control):
    """Info box"""

    html: str
    css_text: str = Field(
        "top: 65px; left: .5em; padding: 5px;", serialization_alias="cssText"
    )


class DrawControl(Control):
    """Draw control"""

    ...


# --- Control type
ControlT = Union[
    Control,
    FullScreenControl,
    ScaleLineControl,
    ZoomSliderControl,
    OverviewMapControl,
    ZoomControl,
    RotateControl,
    ZoomToExtentControl,
    MapTilerGeocodingControl,
    InfoBox,
    DrawControl,
]
