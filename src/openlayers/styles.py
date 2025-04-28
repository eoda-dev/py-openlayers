from __future__ import annotations

from pydantic import BaseModel, Field


class VectorStyle(BaseModel):
    stroke_color: str | list | None = Field("steelblue", serialization_alias="stroke-color")
    stroke_width: float | int | list | None = Field(2, serialization_alias="stroke-width")
    circle_color: str | list | None = Field("steelblue", serialization_alias="circle-color")

