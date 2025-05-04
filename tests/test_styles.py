from openlayers.styles import default_style, FlatStyle

def test_default_vector_style() -> None:
    style = default_style()
    json_def = style.model_dump()

    print(json_def)

    assert json_def["stroke-color"] == "#3399CC"

def test_updates() -> None:
    update = dict(fill_color="green")
    style = default_style().model_copy(update=update)

    print(style.model_dump())
    print(style)
