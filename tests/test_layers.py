from openlayers.layers import TileLayer, VectorLayer
from openlayers.sources import GeoJSONSource, VectorSource


def test_tile_layer() -> None:
    layer = TileLayer(source=dict(foo="bar"))
    print(layer.model_dump())


def test_vector_layer() -> None:
    layer = VectorLayer(
        source=GeoJSONSource(
            url="https://openlayers.org/data/vector/populated-places.json"
        ),
        style={"circle-color": "yellow"},
    )
    print(layer.model_dump())

    assert layer.source.url == "https://openlayers.org/data/vector/populated-places.json"
    assert layer.model_dump()["options"]["source"]["options"]["url"] == "https://openlayers.org/data/vector/populated-places.json"