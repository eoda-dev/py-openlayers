import geopandas as gpd
import pandas as pd

from openlayers.config import DEFAULT_STYLE

from .view import CRS
from .json_defs import VectorSource, WebGLVectorLayer, VectorLayer
from .anywidget import MapWidget

def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = CRS.MERCATOR):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()


@pd.api.extensions.register_dataframe_accessor("ol")
class DataFrameAccessor(object):
    def __init__(self, gdf: gpd.GeoDataFrame) -> None:
        self._gdf = gdf

    def explore(self, style=DEFAULT_STYLE, layer_id: str = "geopandas", **kwargs) -> MapWidget:
        feature_collection = gdf_to_geojson(self._gdf)
        source = VectorSource(geojson=feature_collection)
        layer = WebGLVectorLayer(id=layer_id, style=style, source=source)
        m = MapWidget(**kwargs)
        m.add_layer(layer)
        return m


@pd.api.extensions.register_dataframe_accessor("openlayers")
class DataFrameAccessorAlias(DataFrameAccessor): ...
