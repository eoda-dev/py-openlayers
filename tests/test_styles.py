from openlayers.styles import default_style

def test_vector_style() -> None:
    style = default_style()
    json_def = style.model_dump()

    print(json_def)

    assert json_def["stroke-color"] == "#3B9AB2"
