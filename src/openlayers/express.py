from __future__ import annotations

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

from .abstracts import LayerLike
from .anywidget import MapWidget
from .map import Map
from .models.formats import GPX, KML, Format, GeoJSON
from .models.layers import TileLayer, VectorLayer, WebGLTileLayer, WebGLVectorLayer
from .models.sources import GeoTIFFSource, VectorSource
from .models.view import View
from .styles import FlatStyle, default_style


class GeoTIFFTileLayer(LayerLike):
    """Initialize a new `GeoTIFFTileLayer` instance"""

    def __init__(self, url: str, opacity: float = 0.5):
        source = GeoTIFFSource(sources=[dict(url=url)])
        self._model = WebGLTileLayer(opacity=opacity, source=source)

    @property
    def model(self) -> WebGLTileLayer:
        return self._model

    def to_map(self, *args, **kwargs) -> Map:
        """Initialize a new `Map` instance and add the layer to it"""
        m = Map(*args, **kwargs)
        m.add_layer(self)
        m.set_view_from_source(self.model.id)
        return m


class Vector(LayerLike):
    def __init__(
        self,
        data: str | dict,
        id: str = None,
        style=default_style(),
        fit_bounds: bool = True,
        format: Format = None,
        webgl: bool = True,
        **kwargs,
    ) -> None:
        source = (
            VectorSource(url=data)
            if isinstance(data, str)
            else VectorSource(geojson=data)
        )
        if not format and source.url:
            url = source.url.lower()
            if url.endswith(".kml"):
                format = KML()
            elif url.endswith(".gpx"):
                format = GPX()

        source.format = format or GeoJSON()
        Layer = WebGLVectorLayer if webgl else VectorLayer
        self._model = Layer(
            source=source, id=id, fit_bounds=fit_bounds, style=style, **kwargs
        )

    def explore(self, tooltip: bool = True, **kwargs) -> Map | MapWidget:
        m = Map(**kwargs)
        m.add_layer(self._model)
        if tooltip:
            m.add_default_tooltip()

        return m

    @property
    def model(self) -> VectorLayer | WebGLVectorLayer:
        return self._model


# TODO: Move to VectorLayer
class GeoJSONLayer(LayerLike):
    """Initialize a new `GeoJSONLayer` instance

    Args:
        data (str | dict): Either an URL to a GeoJSON object
            or a dictionary representing a GeoJSON object
        id (str): The ID of the layer. If `None`, a random ID is generated
        style (FlatStyle): The style to be applied to the layer. If `None` a default style is used
        **kwargs (Any): Style arguments that are appended to the `Style` object.
            Latter ones overwrite existing entries
    """

    def __init__(
        self,
        data: str | dict,
        id: str | None = None,
        style: FlatStyle | None = None,
        webgl: bool = True,
        **kwargs,
    ):
        vector_layer_class = WebGLVectorLayer if webgl else VectorLayer
        if isinstance(data, str):
            source = VectorSource(url=data)
        else:
            source = VectorSource(geojson=data)

        self._model = vector_layer_class(
            source=source,
            style=style
            or default_style().model_copy(update=FlatStyle(**kwargs).model_dump2()),
            id=id,
        )

    @property
    def model(self) -> WebGLVectorLayer | VectorLayer:
        return self._model

    def set_icon_style(self) -> Self:
        # TODO: implement
        return self

    def to_map(
        self, lon: float = 0, lat: float = 0, zoom: float | int = 0, **kwargs
    ) -> Map | MapWidget:
        """Initialize a new `Map` instance and add the layer to it

        Args:
            lon (float): The longitude of the initial view state of the map
            lat (float): The latitude of the initial view state of the map
            zoom (float | int): The initial zoom level of the map
            **kwargs (Any): Arguments that are handed over to the `Map` instance
        """
        m = MapWidget(View(center=(lon, lat), zoom=zoom), **kwargs)
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
