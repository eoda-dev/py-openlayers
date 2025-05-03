from __future__ import annotations

import os
from enum import Enum

from pydantic import BaseModel, ConfigDict

from .styles import FlatStyle, default_style

"""
DEFAULT_STYLE = {
    "stroke-color": "steelblue",
    "stroke-width": 3,
    "circle-color": "green",
}
"""


class Backend(Enum):
    STANDALONE = "standalone"
    ANYWIDGET = "anywidget"
    IPYWIDGET = "anywidget"


class Config(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True, validate_default=True, validate_assignment=True
    )

    backend: str | Backend = Backend.ANYWIDGET
    vector_style: FlatStyle = default_style()
    controls: list = list()
    maptiler_api_key_env_var: str = "MAPTILER_API_KEY"

    @property
    def maptiler_api_key(self) -> str:
        return os.environ.get(self.maptiler_api_key_env_var)


config = Config()
