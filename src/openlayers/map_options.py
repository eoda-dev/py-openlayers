from __future__ import annotations

from typing import Union

from pydantic import Field, field_validator

from .abstracts import MyBaseModel
from .controls import Control
from .layers import Layer
from .view import View


class MapOptions(MyBaseModel):
    view: View | None = Field(View(), serialization_alias="viewOptions")
    controls: list[Control | dict] | None = None
    layers: list[Layer | dict] | None

    @field_validator("layers", "controls")
    def validate_layers_and_controls(cls, items) -> list[dict] | None:
        if items is None:
            return

        return [
            item.model_dump() if isinstance(item, Union[Layer, Control]) else item
            for item in items
        ]
