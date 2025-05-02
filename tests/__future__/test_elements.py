from openlayers.__future__.elements import View

def test_view() -> None:
    view = View((3, 5), zoom=12)
    print(view.model_dump())
