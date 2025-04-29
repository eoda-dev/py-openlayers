from __future__ import annotations

from typing import Union
from uuid import uuid4

from pydantic import Field

from .core import OLBaseModel
from .sources import SourceT


# --- Base layer
class Layer(OLBaseModel):
    id: str = Field(default_factory=lambda x: str(uuid4()))
    source: dict | SourceT
    background: str | None = None


# --- Layers
class TileLayer(Layer): ...


class VectorLayer(Layer):
    style: dict | None = None


class WebGLVectorLayer(Layer):
    style: dict | None = None


class WebGLTileLayer(Layer):
    style: dict | None = None


# --- Layer type
LayerT = Union[Layer, TileLayer, VectorLayer, WebGLVectorLayer, WebGLTileLayer]
