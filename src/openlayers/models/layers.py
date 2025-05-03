from __future__ import annotations

from typing import Union
from uuid import uuid4

from pydantic import Field, field_validator

from ..styles import FlatStyle, default_style
from .core import OLBaseModel
from .sources import SourceT


# --- Base layer
class Layer(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))
    source: dict | SourceT
    background: str | None = None
    opacity: float | None = 1.0
    visible: bool | None = True


# --- Layers
class TileLayer(Layer): ...


class VectorLayer(Layer):
    style: dict | FlatStyle = default_style()

    @field_validator("style")
    def validate_style(cls, v):
        if isinstance(v, FlatStyle):
            return v.model_dump()

        return v


class WebGLVectorLayer(VectorLayer): ...


class WebGLTileLayer(Layer):
    style: dict | None = None


# --- Layer type
LayerT = Union[Layer, TileLayer, VectorLayer, WebGLVectorLayer, WebGLTileLayer]
