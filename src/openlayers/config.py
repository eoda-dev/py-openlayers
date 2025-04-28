from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, ConfigDict

from .styles import VectorStyle

DEFAULT_STYLE = {
    "stroke-color": "steelblue",
    "stroke-width": 3,
    "circle-color": "green",
}


class Backend(Enum):
    STANDALONE = "standalone"
    ANYWIDGET = "anywidget"
    IPYWIDGET = "anywidget"


class Config(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    default_backend: Backend = Backend.ANYWIDGET
    default_controls: list = []
    vector_style: VectorStyle = VectorStyle()


config = Config()
