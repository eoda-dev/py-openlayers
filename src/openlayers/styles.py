from __future__ import annotations

import os
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .utils import create_icon_src_from_file


def fix_keys(d: dict) -> dict:
    return {k.replace("_", "-"): v for k, v in d.items() if v is not None}


# TODO: Move to models folder
# See https://openlayers.org/en/latest/apidoc/module-ol_style_flat.html
class FlatStyle(BaseModel):
    """A style object for vector layers

    Underscores in the property names are automatically converted to hyphens.

    Note:
        See [ol/style/flat](https://openlayers.org/en/latest/apidoc/module-ol_style_flat.html)
        for all available style properties.
    """

    model_config = ConfigDict(extra="allow")

    fill_color: str | list | None = None

    stroke_color: str | list | None = None
    stroke_width: float | int | list | None = None

    circle_radius: float | int | list | None = None
    circle_fill_color: str | list | None = None
    circle_stroke_width: float | int | list | None = None
    circle_stroke_color: str | list | None = None

    icon_src: str | Path | list | None = None
    icon_scale: float | int | list | None = None
    icon_color: str | list | None = None
    icon_opacity: float | int | None = Field(None, gt=0, le=1)

    text_value: str | list | None = None
    text_font: str | list | None = None
    text_fill_color: str | list | None = None
    text_stroke_width: float | int | list | None = None
    text_stroke_color: str | list | None = None

    @field_validator("icon_src")
    def validate_icon_src(cls, v) -> str:
        if os.path.isfile(v):
            return create_icon_src_from_file(v)

        return v

    def model_dump(self) -> dict:
        return fix_keys(super().model_dump(exclude_none=True))

    def model_dump2(self) -> dict:
        return super().model_dump(exclude_none=True)


def default_style(**kwargs) -> FlatStyle:
    """Create a default style object for vector layers

    Args:
        **kwargs (Any): Additional style properties or
            updates of the default properties

    Returns:
        A style object
    """
    return FlatStyle(
        fill_color="rgba(255,255,255,0.4)",
        # ---
        stroke_color="#3399CC",
        stroke_width=1.25,
        # ---
        circle_radius=5,
        circle_fill_color="rgba(255,255,255,0.4)",
        circle_stroke_width=1.25,
        circle_stroke_color="#3399CC",
    ).model_copy(update=kwargs)
