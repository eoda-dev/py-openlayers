from openlayers.layers import TileLayer, VectorLayer
from openlayers.sources import VectorSource

def test_tile_layer() -> None:
    layer = TileLayer(source=dict(foo="bar"))
    print(layer.to_dict())

def test_vector_layer() -> None:
    layer = VectorLayer(
            source=VectorSource(url="xyz"),
            style = {"circle-color": "yellow"}
            )
    print(layer.to_dict())

