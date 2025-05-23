from openlayers.map import Map
from openlayers.models.view import View


def test_map() -> None:
    # Prepare
    view = View(center=(2, 2))

    # Act
    m = Map(view)

    # Assert
    print(m.options)
    assert m.options["view"] == view.model_dump()

    assert m.initial_view_state["center"] == (2, 2)
