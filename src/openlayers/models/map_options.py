from __future__ import annotations

from pydantic import BaseModel, ConfigDict, field_validator

from ..abstracts import LayerLike
from .controls import ControlT
from .layers import LayerT
from .view import View


class MapOptions(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True
    )  # Needed to support 'LayerLike'

    view: View | None = View()
    controls: list[dict | ControlT] | None = None
    layers: list[dict | LayerT | LayerLike] | None = None

    @field_validator("layers")
    def validate_layers(cls, layers) -> list[dict | LayerT]:
        layers = [
            layer.model if isinstance(layer, LayerLike) else layer for layer in layers
        ]
        return layers

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
