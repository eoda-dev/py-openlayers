from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, computed_field
from uuid import uuid4
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


# --- Format
class Format(OLBaseModel): ...


class GeoJSON(Format): ...


# --- Sources
class Source(OLBaseModel): ...


class OSM(Source): ...


class VectorSource(Source):
    url: str | None = None
    format: dict | GeoJSON  = GeoJSON()


class GeoTIFFSource(Source):
    normalize: bool | None = None
    sources: list[dict]


SourceT = Union[OSM, VectorSource, GeoTIFFSource]


# --- Layers
class Layer(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))
    source: dict | SourceT


class TileLayer(Layer): ...


class VectorLayer(Layer):
    style: dict | None = None


class WebGLVectorLayer(Layer):
    style: dict | None = None


class WebGLTileLayer(Layer):
    style: dict | None = None


LayerT = Union[Layer, TileLayer, WebGLVectorLayer | WebGLTileLayer]


# --- Control that depends on Layer definitions
class OverviewMapControl(Control):
    layers: list[dict | LayerT]


ControlT = Union[
    Control, FullScreenControl, ScaleLineControl, ZoomSliderControl, OverviewMapControl
]


# ---
class MapOptions(BaseModel):
    view: View | None = Field(View(), serialization_alias="viewOptions")
    controls: list[dict | ControlT] | None = None
    layers: list[dict | LayerT] | None = None

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
