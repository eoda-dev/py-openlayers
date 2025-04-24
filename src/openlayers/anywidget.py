from __future__ import annotations
from pathlib import Path
from typing import Any
import traitlets
from anywidget import AnyWidget

from .json_defs import ControlT, LayerT
from .map import Map
from .view import View


class MapWidget(AnyWidget, Map):
    _esm = Path(__file__).parent / "js" / "openlayers.anywidget.js"
    _css = Path(__file__).parent / "js" / "openlayers.anywidget.css"

    # view_state = traitlets.Dict().tag(sync=True, o=True)
    map_options = traitlets.Dict().tag(sync=True, o=True)
    height = traitlets.Unicode().tag(sync=True, o=True)
    map_clicked = traitlets.Dict().tag(sync=True)
    debug_data = traitlets.Dict().tag(sync=True, o=True)

    def __init__(
        self,
        view: View = View(),
        layers: list[LayerT | dict] | None = None,
        controls: list[ControlT | dict] | None = None,
        height: str = "400px",
        debug_data: dict = None,
        **kwargs,
    ):
        self.debug_data = debug_data or dict()
        AnyWidget.__init__(self, height=height, **kwargs)
        Map.__init__(self, view, layers, controls)

    def add_call(self, method_name: str, *args: Any) -> None:
        call = dict(method=method_name, args=args)
        self.send(call)
