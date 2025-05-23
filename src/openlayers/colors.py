from __future__ import annotations

import json
import os
import random
from typing import Any

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
            print(e)
            return

    return [ColorScheme(name=k, values=v) for k, v in data.items()]


class Color(object):
    @staticmethod
    def random_rgb_colors(n: int) -> list[int]:
        return [tuple([random.randrange(255) for _ in range(3)]) for _ in range(n)]

    @staticmethod
    def random_hex_colors(n: int) -> list[str]:
        return [
            "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])
            for _ in range(n)
        ]

    @classmethod
    def random_hex_colors_by_category(cls, categories: Any) -> list[str]:
        import pandas as pd

        codes = pd.Categorical(categories).codes
        colors = cls.random_hex_colors(len(codes))
        return [colors[code] for code in codes]
