from openlayers.utils import crs_transformer

def test_crs_transformer() -> None:
    lon = -122.4
    lat = 37.74
    
    transformer = crs_transformer()
    center = (lon, lat)
    coords = transformer.transform(*center)

    print(coords)
