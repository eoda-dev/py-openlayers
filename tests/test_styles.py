from pathlib import Path

from openlayers.styles import default_style, FlatStyle

def test_default_vector_style() -> None:
    style = default_style()
    json_def = style.model_dump()

    print(json_def)

    assert json_def["stroke-color"] == "#3399CC"

def test_update_default_style() -> None:
    # update = dict(fill_color="green")
    # style = default_style().model_copy(update=update)

    style = default_style(fill_color="green")

    print(style.model_dump())
    print(style)

def test_icon_style() -> None:
    icon_url = "http://xyz.de/icon.png"

    style = FlatStyle(
        icon_src=icon_url
    )

    dumped_style = style.model_dump()

    print(dumped_style)
    assert dumped_style["icon-src"] == icon_url

def test_icon_from_file() -> None:
    icon_path = Path(__file__).parent / "data" / "icon.png" 
    print(icon_path)

    style = FlatStyle(icon_src=icon_path)
    dumped_style = style.model_dump()

    print(type(style.icon_src))

    print(dumped_style)
