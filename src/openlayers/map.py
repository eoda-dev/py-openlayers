from .view import View
from .map_options import MapOptions

class Map(object):
    def __init__(self, view: View | dict, layers: list = None):
        # self.view_options = view.to_dict()
        self.map_options = MapOptions(view=view, layers=layers).to_dict()

