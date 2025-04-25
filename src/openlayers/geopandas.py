import geopandas as gpd

from .view import CRS


def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = CRS.MERCATOR):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()
