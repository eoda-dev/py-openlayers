from __future__ import annotations

from typing import Any, Literal, Union
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, computed_field

from .view import View


class OLBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self, **kwargs) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True, **kwargs)

    @computed_field(alias="@@type")
    def type(self) -> str:
        return type(self).__name__


# ---Controls
class Control(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))


class FullScreenControl(Control): ...


class ScaleLineControl(Control):
    bar: bool | None = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False


class ZoomSliderControl(Control): ...


class MousePositionControl(Control):
    projection: str | None = "EPSG:4326"


# --- Custom controls
class InfoBox(Control):
    html: str
    css_text: str = Field(
        "top: 65px; left: .5em; padding: 5px;", serialization_alias="cssText"
    )


# --- Format
class Format(OLBaseModel): ...


class GeoJSON(Format): ...


# --- Sources
class Source(OLBaseModel): ...


class OSM(Source): ...


class VectorSource(Source):
    url: str | None = None
    features: list[dict] | None = None
    geojson: dict | None = Field(None, serialization_alias="@@geojson")
    format: dict | GeoJSON = GeoJSON()


class GeoTIFFSource(Source):
    normalize: bool | None = None
    sources: list[dict]


SourceT = Union[OSM, VectorSource, GeoTIFFSource]


# --- Layers
class Layer(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))
    source: dict | SourceT
    background: str | None = None


class TileLayer(Layer): ...


class VectorLayer(Layer):
    style: dict | None = None


class WebGLVectorLayer(Layer):
    style: dict | None = None


class WebGLTileLayer(Layer):
    style: dict | None = None


LayerT = Union[Layer, TileLayer, VectorLayer, WebGLVectorLayer, WebGLTileLayer]


# --- Control that depends on Layer definitions
class OverviewMapControl(Control):
    layers: list[dict | LayerT]


ControlT = Union[
    Control,
    FullScreenControl,
    ScaleLineControl,
    ZoomSliderControl,
    OverviewMapControl,
    InfoBox,
]


# ---
class MapOptions(BaseModel):
    view: View | None = Field(View(), serialization_alias="viewOptions")
    controls: list[dict | ControlT] | None = None
    layers: list[dict | LayerT] | None = None

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
