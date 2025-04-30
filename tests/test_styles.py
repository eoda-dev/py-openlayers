from openlayers.styles import VectorStyle

def test_vector_style() -> None:
    style = VectorStyle()
    json_def = style.model_dump()

    print(json_def)

    assert json_def["stroke-color"] == "#3B9AB2"
