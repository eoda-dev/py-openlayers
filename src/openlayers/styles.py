from __future__ import annotations

from pydantic import BaseModel

class VectorStyle(BaseModel):
    stroke_color: str | list | None = "steelblue"
    stroke_width: float | int | list | None = 2
    circle_color: str | list | None = "steelblue"
