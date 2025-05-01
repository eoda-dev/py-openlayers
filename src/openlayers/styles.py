from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


def fix_keys(d: dict) -> dict:
    return {k.replace("_", "-"): v for k, v in d.items() if v is not None}

# TODO: Move to models folder
class FlatStyle(BaseModel):
    model_config = ConfigDict(extra="allow")

    fill_color: str | list | None = None

    stroke_color: str | list | None = None
    stroke_width: float | int | list | None = None

    circle_radius: float | int | list | None = None
    circle_fill_color: str | list | None = None
    circle_stroke_width: float | int | list | None = None
    circle_stroke_color: str | list | None = None

    icon_src: str | list | None = None
    icon_color: str | list | None = None
    icon_opacity: float | int | None = Field(None, gt=0, le=1)

    def model_dump(self) -> dict:
        return fix_keys(super().model_dump(exclude_none=True))


def default_style() -> FlatStyle:
    return FlatStyle(
        fill_color="#0B775E",
        stroke_color="#3B9AB2",
        stroke_width=1.25,
        circle_radius=5,
        circle_fill_color="#EBCC2A",
        circle_stroke_width=1.25,
        circle_stroke_color="#F21A00",
    )


class CircleStyle(FlatStyle): ...


class IconStyle(FlatStyle): ...


class FillStyle(FlatStyle): ...
