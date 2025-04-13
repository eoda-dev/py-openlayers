from openlayers.layers import TileLayer


def test_tile_layer() -> None:
    layer = TileLayer(source=dict(foo="bar"))
    print(layer.to_dict())
