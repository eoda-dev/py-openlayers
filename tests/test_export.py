from openlayers.export import HTMLTemplate
from openlayers.map import Map, View


def test_dummy_export() -> None:
    css = "#map {color: black;}"
    js = "console.log('openlayers');"

    template = HTMLTemplate(css=css, js=js)
    output = template.render()
    print(output)


def test_to_html() -> None:
    template = HTMLTemplate()
    output = template.render()

    print(output)


def _test_save_html() -> None:
    m = Map(View())
    print(m.options)
    path = m.save(preview=True)
    print("path", path)
