from openlayers.map import Map
from openlayers.view import View


def test_map() -> None:
    view = View(center=(2, 2))
    m = Map(view)
    print(m._view)
