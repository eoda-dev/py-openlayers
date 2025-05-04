from __future__ import annotations

from .models.layers import WebGLVectorLayer
from .models.sources import VectorSource
from .styles import FlatStyle


class SimpleLayer(object): ...


class GeoJSONLayer(object): ...


class TileLayer(object): ...


class OSMBaseLayer(object): ...


class IconLayer(object):
    def __init__(
        self,
        url: str = None,
        data: dict = None,
        icon_src: str = None,
        icon_color: str = None,
        icon_opacity: float = 1,
    ):
        style = FlatStyle(
            icon_src=icon_src, icon_color=icon_color, icon_opacity=icon_opacity
        )
        source = VectorSource(url=url, geojson=data)
        self._model = WebGLVectorLayer(source=source, style=style)

    def model_dump(self):
        return self._model.model_dump()

    def to_map(self): ...
