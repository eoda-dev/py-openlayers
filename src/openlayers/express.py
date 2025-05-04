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
        id: str = "icon-layer",
        style: FlatStyle = None
    ):
        style = style or FlatStyle(
            icon_src=icon_src, icon_color=icon_color, icon_opacity=icon_opacity
        )
        source = VectorSource(url=url, geojson=data)
        self._model = WebGLVectorLayer(source=source, style=style, id=id)

    @property
    def model(self) -> WebGLVectorLayer:
        return self._model

    def to_map(self): ...


class PolygonLayer(LayerLike):
    def __init__(
        self,
        url: str,
        fill_color: str = "rgba(255,255,255,0.4)",
        stroke_color="#3399CC",
        stroke_width=1.25,
        id: str = "polygon-layer",
        style: FlatStyle = None
    ):
        style = style or FlatStyle(
            fill_color=fill_color, stroke_color=stroke_color, stroke_width=stroke_width
        )
        source = VectorSource(url=url)
        self._model = WebGLVectorLayer(source=source, style=style, id=id)

    @property
    def model(self) -> WebGLVectorLayer:
        return self._model


class CirleLayer(LayerLike): ...


class LineLayer(LayerLike): ...
