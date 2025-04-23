from .abstracts import MyBaseModel, Source
from pydantic import ConfigDict
from .sources import VectorSource

class TileLayer(MyBaseModel):
    source: dict | Source

class VectorLayer(MyBaseModel):
    model_config = ConfigDict(strict=True)

    source: dict | Source | VectorSource
    style: dict

