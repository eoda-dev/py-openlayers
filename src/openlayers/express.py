from __future__ import annotations

from .models.layers import WebGLVectorLayer, VectorLayer
from .models.sources import VectorSource
from .styles import FlatStyle, default_style
from .abstracts import LayerLike
from .map import Map


class GeoJSONLayer(LayerLike):
    def __init__(
        self,
        data: str | dict,
        id: str | None = "geojson-layer",
        style: FlatStyle | None = None,
        **kwargs,
    ):
        if isinstance(data, str):
            source = VectorSource(url=data)
        else:
            source = VectorSource(geojson=data)

        self._model = WebGLVectorLayer(
            source=source,
            style=style
            or default_style().model_copy(update=FlatStyle(**kwargs).model_dump2()),
            id=id,
        )

    @property
    def model(self) -> WebGLVectorLayer | VectorLayer:
        return self._model

    def to_map(self):
        return Map(layers=[self])


class TileLayer(object): ...


class OSMBaseLayer(object): ...


# TODO: Should also be subclass of GeoJSONLayer
class XXIconLayer_(LayerLike):
    def __init__(
        self,
        url: str = None,
        data: dict = None,
        icon_src: str = None,
        icon_color: str = None,
        icon_opacity: float = 1,
        id: str = "icon-layer",
        style: FlatStyle = None,
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


# TODO: Deprecated: Use FillLayer instead
class PolygonLayer(GeoJSONLayer):
    def __init__(
        self,
        url: str,
        fill_color: str = "rgba(255,255,255,0.4)",
        stroke_color="#3399CC",
        stroke_width=1.25,
        id: str = "polygon-layer",
        style: FlatStyle = None,
    ):
        style = style or FlatStyle(
            fill_color=fill_color, stroke_color=stroke_color, stroke_width=stroke_width
        )
        source = VectorSource(url=url)
        self._model = WebGLVectorLayer(source=source, style=style, id=id)

    @property
    def model(self) -> WebGLVectorLayer:
        return self._model


class CircleLayer(GeoJSONLayer):
    def __init__(
        self,
        data: str | dict,
        circle_fill_color: str | None = None,
        id: str | None = "circle-layer",
        style: FlatStyle | None = None,
        **kwargs,
    ):
        super().__init__(data, id, style, circle_fill_color=circle_fill_color, **kwargs)


class FillLayer(GeoJSONLayer):
    def __init__(
        self,
        data: str | dict,
        fill_color: str | None = None,
        id: str | None = "fill-layer",
        style: FlatStyle | None = None,
        **kwargs,
    ):
        super().__init__(data, id, style, fill_color=fill_color, **kwargs)


class LineLayer(GeoJSONLayer): ...


class IconLayer(GeoJSONLayer):
    def __init__(
        self,
        data: str | dict,
        icon_src: str,
        id: str | None = "icon-layer",
        style: FlatStyle | None = None,
        **kwargs,
    ):
        super().__init__(data, id, style, icon_src=icon_src, **kwargs)
