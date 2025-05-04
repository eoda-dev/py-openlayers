import geopandas as gpd
import pandas as pd

from .anywidget import MapWidget
from .models.layers import VectorLayer, WebGLVectorLayer
from .models.sources import VectorSource
from .models.view import Projection
from .styles import FlatStyle, default_style


def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = Projection.WEB_MERCATOR):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()


@pd.api.extensions.register_dataframe_accessor("ol")
class OLAccessor:
    def __init__(self, gdf: gpd.GeoDataFrame) -> None:
        self._gdf = gdf

    def to_source(self) -> VectorSource:
        feature_collection = gdf_to_geojson(self._gdf)
        source = VectorSource(geojson=feature_collection)
        return source

    def to_layer(
        self,
        style: FlatStyle | dict = None,
        layer_id: str = "geopandas",
        webgl: bool = True,
        **kwargs
    ) -> VectorLayer | WebGLVectorLayer:
        style = style or default_style()
        layer_class = WebGLVectorLayer if webgl else VectorLayer
        layer = layer_class(id=layer_id, style=style, source=self.to_source(), **kwargs)
        return layer

    def explore(
        self,
        style: FlatStyle | dict = None,
        tooltip: bool | str = True,
        layer_id: str = "geopandas",
        webgl: bool = True,
        **kwargs,
    ) -> MapWidget:
        layer = self.to_layer(style=style, layer_id=layer_id, webgl=webgl)

        m = MapWidget(**kwargs)
        m.add_layer(layer)
        if isinstance(tooltip, str):
            m.add_tooltip(tooltip)
        elif tooltip:
            m.add_default_tooltip()

        return m


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
