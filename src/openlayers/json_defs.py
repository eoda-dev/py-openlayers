from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field, computed_field

from .view import View


class OLBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)

    @computed_field(alias="@@type")
    def type(self) -> str:
        return type(self).__name__


class Control(OLBaseModel): ...


class FullScreenControl(Control): ...


class ScaleLineControl(Control):
    bar: bool | None = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False


# ---
class Source(OLBaseModel): ...


class OSM(Source): ...


class ZoomSliderControl(Control): ...


class MousePositionControl(Control):
    projection: str | None = "EPSG:4326"


# ---
class Layer(OLBaseModel):
    source: OSM | dict


class TileLayer(Layer): ...


LayerT = Union[Layer, TileLayer]
ControlT = Union[Control, FullScreenControl, ScaleLineControl]


# ---
class MapOptions(BaseModel):
    view: View | None = Field(View(), serialization_alias="viewOptions")
    controls: list[ControlT | dict] | None = None
    layers: list[LayerT | dict] | None = None

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
