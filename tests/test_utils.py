from openlayers.utils import default_crs_transformer

def test_crs_transformer() -> None:
    lon = -122.4
    lat = 37.74
    
    transformer = default_crs_transformer()
    center = (lon, lat)
    coords = transformer.transform(*center)

    print(coords)
