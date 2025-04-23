from __future__ import annotations

from .abstracts import MyBaseModel, Source, Layer
# from pydantic import ConfigDict
# from .sources import VectorSource

class TileLayer(Layer): ...
    # source: dict | Source

"""
class VectorLayer(MyBaseModel):
    model_config = ConfigDict(strict=True)

    source: dict | Source | VectorSource
    style: dict
"""

class VectorLayer(Layer):
    style: dict | None = None
