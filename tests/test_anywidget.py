from openlayers.anywidget import MapWidget


def test_map_widget() -> None:
    map = MapWidget()

    print(map._esm)
    print(map._css)
