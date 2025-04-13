from .view import View


class Map(object):
    def __init__(self, view: View | dict):
        self._view = view
