from __future__ import annotations

from .abstracts import LayerLike
from .map import Map
from .models.layers import VectorLayer, WebGLVectorLayer
from .models.sources import VectorSource
from .models.view import View
from .styles import FlatStyle, default_style


class GeoJSONLayer(LayerLike):
    def __init__(
        self,
        data: str | dict,
        id: str | None = None,
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

    def to_map(
        self, lon: float = 0, lat: float = 0, zoom: float | int = 0, **kwargs
    ) -> Map:
        m = Map(View(center=(lon, lat), zoom=zoom), **kwargs)
        m.add_layer(self)
        return m


# class TileLayer(object): ...


# class OSMBaseLayer(object): ...


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


# class LineLayer(GeoJSONLayer): ...


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
