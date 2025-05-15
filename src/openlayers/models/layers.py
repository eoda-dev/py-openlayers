from __future__ import annotations

from typing import Union
from uuid import uuid4

from pydantic import Field, field_validator

from ..styles import FlatStyle, default_style
from .core import OLBaseModel
from .sources import SourceT


# --- Base layer
class Layer(OLBaseModel):
    id: str | None = None
    source: dict | SourceT
    background: str | None = None
    opacity: float | None = 1.0
    visible: bool | None = True
    z_index: int | None = Field(None, serialization_alias="zIndex")

    @field_validator("id")
    def validate_id(cls, v) -> str:
        if v is None:
            return uuid4().hex[0:10]

        return v


# --- Layers
class TileLayer(Layer): ...


# TODO: Inherit from `VectorTileLayer`
class VectorLayer(Layer):
    style: dict | FlatStyle | None = default_style()
    fit_bounds: bool = Field(False, serialization_alias="fitBounds")

    @field_validator("style")
    def validate_style(cls, v):
        if isinstance(v, FlatStyle):
            return v.model_dump()

        return v


class WebGLVectorLayer(VectorLayer): ...


class VectorTileLayer(Layer):
    style: dict | FlatStyle | None = None

    @field_validator("style")
    def validate_style(cls, v):
        if isinstance(v, FlatStyle):
            return v.model_dump()

        return v


class WebGLVectorTileLayer(VectorTileLayer): ...


class WebGLTileLayer(Layer):
    # See https://openlayers.org/en/latest/apidoc/module-ol_layer_WebGLTile.html#~Style
    style: dict | None = None


# --- Layer type
LayerT = Union[
    Layer,
    TileLayer,
    VectorLayer,
    WebGLVectorLayer,
    WebGLTileLayer,
    VectorTileLayer,
    WebGLVectorTileLayer,
]
