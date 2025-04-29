from __future__ import annotations

import json
import os

from pydantic import BaseModel

COLOR_SCHEMES = "https://raw.githubusercontent.com/python-visualization/branca/refs/heads/main/branca/_schemes.json"


class ColorScheme(BaseModel):
    name: str
    values: list[str]


def read_color_schemes(fn: str = None) -> list[ColorScheme]:
    fn = fn or COLOR_SCHEMES
    if os.path.isfile(fn):
        with open(fn, "r") as f:
            data = json.load(f)

    else:
        try:
            import requests

            data = requests.get(fn).json()
        except ImportError as e:
            return

    return [ColorScheme(name=k, values=v) for k, v in data.items()]
