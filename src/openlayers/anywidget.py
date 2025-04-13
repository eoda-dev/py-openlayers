import traitlets
from anywidget import AnyWidget
from pathlib import Path

from .map import Map
from .view import View

class MapWidget(AnyWidget, Map):
    _esm = Path(__file__).parent / "js" / "openlayers.anywidget.js"
    _css = Path(__file__).parent / "js" / "openlayers.anywidget.css"

    view_options = traitlets.Dict().tag(sync=True, o=True)
    height = traitlets.Unicode("600px").tag(sync=True, o=True)

    def __init__(self, view: View, height: str = "400px", **kwargs):
        AnyWidget.__init__(self, height=height, **kwargs)
        Map.__init__(self, view)

