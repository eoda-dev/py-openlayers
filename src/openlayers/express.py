from __future__ import annotations

from .abstracts import LayerLike
from .map import Map
from .models.layers import VectorLayer, WebGLVectorLayer, WebGLTileLayer, TileLayer
from .models.sources import VectorSource, GeoTIFFSource
from .models.view import View
from .styles import FlatStyle, default_style


class GeoTIFFTileLayer(LayerLike):
    """Initialize a new `GeoTIFFTileLayer` instance"""

    def __init__(self, url: str, opacity: float = 0.5, webgl: bool = True):
        tile_layer_callable = WebGLTileLayer if webgl else TileLayer
        source = GeoTIFFSource(sources=[dict(url=url)])
        self._model = tile_layer_callable(opacity=opacity, source=source)

    @property
    def model(self) -> WebGLTileLayer | TileLayer:
        return self._model

    def to_map(self, *args, **kwargs) -> Map:
        m = Map(*args, **kwargs)
        m.add_layer(self)
        # m.add_call("setViewFromSource", self.model.id)
        m.set_view_from_source(self.model.id)
        return m


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
        """Initialize a new `Map` instance and add the layer to it

        Args:
            lon (float): The longitude of the initial view state of the map
            lat (float): The latitude of the initial view state of the map
            zoom (float | int): The initial zoom level of the map
            **kwargs (Any): Arguments that are handed over to the `Map` instance
        """
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
