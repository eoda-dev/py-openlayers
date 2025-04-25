import geopandas as gpd

CRS = "EPSG:3857"

def gdf_to_geojson(data: gpd.GeoDataFrame, crs: str | None = CRS):
    if crs:
        data = data.to_crs(crs)

    return data.to_geo_dict()
