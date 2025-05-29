from __future__ import annotations

from typing import Union
from uuid import uuid4

from pydantic import Field, field_validator

from ..styles import FlatStyle, default_style
from .core import OLBaseModel
from .sources import SourceT


# --- Base layer
class Layer(OLBaseModel):
    """A base class for creating OL layers"""

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


class VectorTileLayer(Layer):
    style: dict | FlatStyle | list | None = default_style()

    @field_validator("style")
    def validate_style(cls, v):
        if isinstance(v, FlatStyle):
            return v.model_dump()

        return v


class VectorLayer(VectorTileLayer):
    """A layer for rendering vector sources"""

    # style: dict | FlatStyle | None = default_style()
    fit_bounds: bool = Field(False, serialization_alias="fitBounds")


class VectorImageLayer(VectorLayer):
    """A layer for rendering vector sources

    This layer type provides great performance during panning and zooming,
    but point symbols and texts are always rotated with the view and pixels are scaled during zoom animations.

    Note:
        See also [VectorImageLayer](https://openlayers.org/en/latest/apidoc/module-ol_layer_VectorImage-VectorImageLayer.html)
    """

    image_ratio: int | None = Field(None, serialization_alias="imageRatio")


class WebGLVectorLayer(VectorLayer):
    """A layer for rendering vector sources using WebGL"""

    ...


class WebGLVectorTileLayer(VectorTileLayer): ...


class WebGLTileLayer(Layer):
    """WebGLTile layer

    Note:
        See [WebGLTile](https://openlayers.org/en/latest/apidoc/module-ol_layer_WebGLTile.html) for details.
    """

    style: dict | None = None


class HeatmapLayer(Layer):
    radius: int | list | None = 8
    blur: int | list | None = 15
    weight: str | list | None = "weight"


# --- Layer type
LayerT = Union[
    Layer,
    TileLayer,
    VectorLayer,
    WebGLVectorLayer,
    WebGLTileLayer,
    VectorTileLayer,
    WebGLVectorTileLayer,
    VectorImageLayer,
    HeatmapLayer,
]
