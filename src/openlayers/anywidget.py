from __future__ import annotations

from pathlib import Path
from typing import Any

import traitlets
from anywidget import AnyWidget

from .map import Map
from .models.controls import ControlT, LayerT
from .models.view import View


class MapWidget(Map, AnyWidget):
    """Initialize a new `MapWidget`instance

    Note:
        See [Map](openlayers.Map) for details.
    """

    _esm = Path(__file__).parent / "js" / "openlayers.anywidget.js"
    _css = Path(__file__).parent / "js" / "openlayers.anywidget.css"

    height = traitlets.Unicode().tag(sync=True)
    calls = traitlets.List().tag(sync=True)
    created = traitlets.Bool().tag(sync=True)
    options = traitlets.Dict().tag(sync=True)
    clicked = traitlets.Dict().tag(sync=True)
    view_state = traitlets.Dict().tag(sync=True)
    metadata = traitlets.Dict().tag(sync=True)

    # TODO: Move to features as well
    # features_selected = traitlets.List().tag(sync=True)

    features = traitlets.Dict().tag(sync=True)

    def __init__(
        self,
        view: View = View(),
        layers: list[LayerT | dict] | None = None,
        controls: list[ControlT | dict] | None = None,
        height: str = "400px",
        **kwargs,
    ):
        self.created = False
        self.calls = []

        Map.__init__(self, view, layers, controls)
        AnyWidget.__init__(self, height=height, **kwargs)

    def add_call(self, method_name: str, *args: Any) -> None:
        call = dict(method=method_name, args=args)
        if self.created:
            return self.send(call)

        self.calls = self.calls + [call]


def map_widget(*args, **kwargs) -> MapWidget:
    return MapWidget(*args, **kwargs)
