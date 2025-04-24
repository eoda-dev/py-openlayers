from .layers import TileLayer
from .map_options import MapOptions
from .sources import OSM
from .view import View


class Map(object):
    def __init__(
        self,
        view: View | dict,
        layers: list | None = None,
        controls: list | None = None,
    ):
        if layers is None:
            layers = [TileLayer(source=OSM())]

        self.map_options = MapOptions(
            view=view, layers=layers, controls=controls
        ).to_dict()
