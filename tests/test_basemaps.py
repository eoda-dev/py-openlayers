from openlayers.basemaps import Carto
from openlayers.layers import TileLayer, BasemapLayer

def test_basemap_layer() -> None:
    layer = BasemapLayer.carto()

    # print(layer)

    layer = BasemapLayer(Carto.DARK_ALL)
    print(layer.model.model_dump())

    assert isinstance(layer.model, TileLayer)
    assert layer.model.id == "carto-dark-all"
