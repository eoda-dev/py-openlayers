from __future__ import annotations

from pydantic import BaseModel, Field

from .controls import ControlT
from .layers import LayerT
from .view import View


class MapOptions(BaseModel):
    view: View | None = View() # Field(View(), serialization_alias="viewOptions")
    controls: list[dict | ControlT] | None = None
    layers: list[dict | LayerT] | None = None

    def model_dump(self) -> dict:
        return super().model_dump(exclude_none=True, by_alias=True)
