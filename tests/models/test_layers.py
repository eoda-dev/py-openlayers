from openlayers.layers import TileLayer, VectorLayer
from openlayers.sources import VectorSource


def test_tile_layer() -> None:
    layer = TileLayer(source=dict(foo="bar"))
    print(layer.model_dump())


def test_vector_layer() -> None:
    # Prepare
    geojson_url = "https://openlayers.org/data/vector/populated-places.json"

    # Act
    vector_layer = VectorLayer(
        source=VectorSource(url=geojson_url),
        style={"circle-color": "yellow"},
    )
    json_def = vector_layer.model_dump()

    # Assert
    print(json_def)

    assert vector_layer.source.url == geojson_url
    assert json_def["source"]["url"] == geojson_url
    assert json_def["@@type"] == "VectorLayer"
