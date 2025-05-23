from openlayers.basemaps import Carto, CartoBasemapLayer
from openlayers.layers import TileLayer, BasemapLayer

def test_basemap_layer() -> None:
    layer = BasemapLayer()

    # print(layer)

    layer = CartoBasemapLayer(Carto.DARK_ALL)
    print(layer.model.model_dump())

    assert isinstance(layer.model, TileLayer)
    assert layer.model.id == "carto-dark-all"
