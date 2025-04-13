from anywidget import AnyWidget
from pathlib import Path

class MapWidget(AnyWidget):
    _esm = Path(__file__).parent / "js" / "openlayers.anywidget.js"
    _css = Path(__file__).parent / "js" / "openlayers.anywidget.css"

