from openlayers.sources import GeoJSONSource, OSM
from openlayers.controls import ScaleLineControl
from openlayers.layers import TileLayer, VectorLayer
from openlayers.map import MapOptions

def test_vector_layer() -> None:
    #vector_layer = VectorLayer(
    #    source=GeoJSONSource(
    #        url="https://openlayers.org/data/vector/populated-places.json"
    #    ),
    #    style={"circle-color": "yellow"},
    #)
    # print(vector_layer.model_dump())

    # assert vector_layer.source["options"]["url"] == "https://openlayers.org/data/vector/populated-places.json"
    # assert vector_layer.model_dump()["options"]["source"]["options"]["url"] == "https://openlayers.org/data/vector/populated-places.json"

    map_options = MapOptions(
        layers=[TileLayer(source=OSM())],
        controls=[ScaleLineControl(bar=True)]
    ).model_dump()

    print(map_options)
    print(ScaleLineControl(bar=True).model_dump())
