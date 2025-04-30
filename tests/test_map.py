from openlayers.map import Map
from openlayers.view import View
# from openlayers.models.view import View


def test_map() -> None:
    # Prepare
    view = View(center=(2, 2))

    # Act
    m = Map(view)

    # Assert
    print(m.map_options)
    assert m.map_options["viewOptions"] == view.model_dump()
