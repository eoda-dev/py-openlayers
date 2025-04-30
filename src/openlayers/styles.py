from __future__ import annotations

from pydantic import BaseModel


def fix_keys(d: dict) -> dict:
    return {k.replace("_", "-"): v for k, v in d.items() if v is not None}


class Style(BaseModel):
    def model_dump(self) -> dict:
        return fix_keys(super().model_dump())


class VectorStyle(Style):
    fill_color: str | list | None = "#0B775E"
    stroke_color: str | list | None = "#3B9AB2"
    stroke_width: float | int | list | None = 1.25

    circle_radius: float | int | list | None = 5
    circle_fill_color: str | list | None = "#EBCC2A"
    circle_stroke_width: float | int | list | None = 1.25
    circle_stroke_color: str | list | None = "#F21A00"
