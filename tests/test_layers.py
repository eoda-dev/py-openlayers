from openlayers.layers import TileLayer, VectorLayer
from openlayers.sources import GeoJSONSource, VectorSource, OSM
from openlayers.map_options import MapOptions

def test_tile_layer() -> None:
    layer = TileLayer(source=dict(foo="bar"))
    print(layer.model_dump())


def test_vector_layer() -> None:
    vector_layer = VectorLayer(
        source=GeoJSONSource(
            url="https://openlayers.org/data/vector/populated-places.json"
        ),
        style={"circle-color": "yellow"},
    )
    print(vector_layer.model_dump())

    assert vector_layer.source["options"]["url"] == "https://openlayers.org/data/vector/populated-places.json"
    assert vector_layer.model_dump()["options"]["source"]["options"]["url"] == "https://openlayers.org/data/vector/populated-places.json"

    # print(MapOptions(layers=[vector_layer, TileLayer(source=OSM())]).model_dump())
