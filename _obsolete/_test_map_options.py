from openlayers.sources import OSM
from openlayers.controls import ScaleLineControl
from openlayers.layers import TileLayer
from openlayers.map_options import MapOptions

def _test_vector_layer() -> None:
    # Act
    map_options = MapOptions(
        layers=[TileLayer(source=OSM())],
        controls=[ScaleLineControl(bar=True)]
    )


    # Assert
    print(map_options)
    assert map_options.layers[0].type == "TileLayer"
    assert map_options.layers[0].source.type == "OSM"
