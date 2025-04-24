from .json_defs import OSM, MapOptions, TileLayer, View, LayerT, ControlT


class Map(object):
    def __init__(
        self,
        view: View | dict,
        layers: list[LayerT | dict] | None = None,
        controls: list[ControlT | dict] | None = None,
    ):
        if layers is None:
            layers = [TileLayer(source=OSM())]

        self.map_options = MapOptions(
            view=view, layers=layers, controls=controls
        ).model_dump()
