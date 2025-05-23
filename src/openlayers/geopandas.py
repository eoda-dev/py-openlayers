from __future__ import annotations

from typing import TYPE_CHECKING, Self

import geopandas as gpd
import pandas as pd

from .anywidget import MapWidget
from .colors import Color
from .models.layers import VectorLayer, WebGLVectorLayer
from .models.sources import VectorSource
from .models.view import Projection
from .styles import FlatStyle, default_style

if TYPE_CHECKING:
    from .models.controls import ControlT

COLOR_COLUMN = "color"


def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = Projection.MERCATOR):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()


@pd.api.extensions.register_dataframe_accessor("ol")
class OLAccessor:
    """Create a new `OLAccessor` instance

    Args:
        gdf (gpd.GeoDataFrame): The `GeoDataFrame`,
            to which the `openlayers` extension is added
    """

    def __init__(self, gdf: gpd.GeoDataFrame) -> None:
        self._gdf = gdf
        self._default_style = default_style()

    def to_source(self) -> VectorSource:
        """Return data frame as OL vector source

        Returns:
            An OL vector source
        """
        feature_collection = gdf_to_geojson(self._gdf)
        source = VectorSource(geojson=feature_collection)
        return source

    def to_layer(
        self,
        style: FlatStyle | dict = None,
        layer_id: str = "geopandas",
        fit_bounds: bool = True,
        webgl: bool = True,
        **kwargs,
    ) -> VectorLayer | WebGLVectorLayer:
        """Return data frame as OL vector layer

        Returns:
            An OL vector layer
        """
        style = style or self._default_style
        layer_class = WebGLVectorLayer if webgl else VectorLayer
        layer = layer_class(
            id=layer_id,
            style=style,
            fit_bounds=fit_bounds,
            source=self.to_source(),
            **kwargs,
        )
        return layer

    def explore(
        self,
        style: FlatStyle | dict = None,
        tooltip: bool | str = True,
        controls: list[ControlT | dict] = None,
        layer_id: str = "geopandas",
        fit_bounds: bool = True,
        webgl: bool = True,
        **kwargs,
    ) -> MapWidget:
        """Create a vector layer and add it to a new `Map` instance

        Args:
            style (FlatStyle | dict): The style applied to the layer.
                If `None`, a default style is used
            tooltip (bool | str): Whether a tooltip should be added to the map.
                Either `True` to add a default tooltip,
                or a mustache template string to add a custom tooltip
            controls (list[ControlT | dict]): Controls initially added to the map
            layer_id (str): The ID of the layer
            fit_bounds (bool): Whether to fit bounds
            webgl (bool): Whether the layer should be added to the map
                as `WebGLVectorLayer` or as `VectorLayer`

        Returns:
            A new `MapWidget` instance
        """
        layer = self.to_layer(
            style=style, layer_id=layer_id, fit_bounds=fit_bounds, webgl=webgl
        )

        m = MapWidget(controls=controls, **kwargs)
        m.add_layer(layer)
        if isinstance(tooltip, str):
            m.add_tooltip(tooltip)
        elif tooltip:
            m.add_default_tooltip()

        return m

    def color_category(self, column: str) -> Self:
        self._gdf[COLOR_COLUMN] = Color.random_hex_colors_by_category(self._gdf[column])
        self._default_style.fill_color = ["get", COLOR_COLUMN]
        self._default_style.circle_fill_color = ["get", COLOR_COLUMN]
        return self

    def icon(self, icon_src: str, icon_scale: float = 1, **kwargs) -> Self:
        # TODO: Use style model instead
        self._default_style = {"icon-src": icon_src, "icon-scale": icon_scale} | kwargs
        return self


@pd.api.extensions.register_dataframe_accessor("openlayers")
class OpenLayersAccessor(OLAccessor): ...


# Custom extentsion, as Pylance cannot deal with the registered extensions
# See also https://github.com/microsoft/pylance-release/issues/1112
class GeoDataFrame(gpd.GeoDataFrame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ol = OLAccessor(self)


def read_file(*args, **kwargs) -> GeoDataFrame:
    return GeoDataFrame(gpd.read_file(*args, **kwargs))
