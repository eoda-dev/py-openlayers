import geopandas as gpd
import pandas as pd

from .anywidget import MapWidget
from .models.layers import VectorLayer, WebGLVectorLayer
from .models.sources import VectorSource
from .models.view import Projection
from .styles import FlatStyle, default_style

# from .config import DEFAULT_STYLE


def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = Projection.WEB_MERCATOR):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()


@pd.api.extensions.register_dataframe_accessor("ol")
class OLAccessor(object):
    def __init__(self, gdf: gpd.GeoDataFrame) -> None:
        self._gdf = gdf

    def explore(
        self, style=default_style(), layer_id: str = "geopandas", **kwargs
    ) -> MapWidget:
        if isinstance(style, FlatStyle):
            style = style.model_dump()

        feature_collection = gdf_to_geojson(self._gdf)
        source = VectorSource(geojson=feature_collection)
        layer = WebGLVectorLayer(id=layer_id, style=style, source=source)
        m = MapWidget(**kwargs)
        m.add_layer(layer)
        return m


@pd.api.extensions.register_dataframe_accessor("openlayers")
class OpenLayersAccessor(OLAccessor): ...
