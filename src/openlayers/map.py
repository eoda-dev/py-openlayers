from .view import View


class Map(object):
    def __init__(self, view: View | dict):
        self.view_options = view.to_dict()

