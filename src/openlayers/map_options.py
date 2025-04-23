from __future__ import annotations

from pydantic import Field, field_validator

from .layers import Layer

from .abstracts import MyBaseModel
from .view import View

class MapOptions(MyBaseModel):
    view: View | None = Field(View(), serialization_alias="viewOptions")
    controls: list[dict] | None = None
    layers: list[Layer | dict] | None = None

    @field_validator("layers")
    def validate_layers(cls, layers) -> list[dict]:
        return [l.model_dump() if isinstance(l, Layer) else l for l in layers]
