from __future__ import annotations

from .models.layers import WebGLVectorLayer
from .models.sources import VectorSource
from .styles import FlatStyle
from .abstracts import LayerLike

# class SimpleLayer(LayerLike): ...


class GeoJSONLayer(object): ...


class TileLayer(object): ...


class OSMBaseLayer(object): ...


class IconLayer(LayerLike):
    def __init__(
        self,
        url: str = None,
        data: dict = None,
        icon_src: str = None,
        icon_color: str = None,
        icon_opacity: float = 1,
        id: str = "icon-layer"
    ):
        style = FlatStyle(
            icon_src=icon_src, icon_color=icon_color, icon_opacity=icon_opacity
        )
        source = VectorSource(url=url, geojson=data)
        self._model = WebGLVectorLayer(source=source, style=style, id=id)

    def model_dump(self):
        return self._model.model_dump()

    def to_map(self): ...
