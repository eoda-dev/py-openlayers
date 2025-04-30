from __future__ import annotations

import webbrowser
from pathlib import Path
from typing import Any

from .export import HTMLTemplate, write_file
from .models.sources import OSM
from .models.controls import ControlT
from .models.layers import LayerT, TileLayer
from .models.map_options import MapOptions
from .models.view import View


class Map(object):
    def __init__(
        self,
        view: View | dict = View(),
        layers: list[LayerT | dict] | None = None,
        controls: list[ControlT | dict] | None = None,
    ):
        self._calls = []
        if layers is None:
            layers = [TileLayer(id="osm", source=OSM())]

        self.map_options = MapOptions(
            view=view, layers=layers, controls=controls
        ).model_dump()

    # 'apply_call_to_map'
    def add_call(self, method_name: str, *args: Any) -> None:
        call = dict(method=method_name, args=args)
        self._calls.append(call)

    # 'apply_call_to_layer'
    def add_layer_call(self, layer_id: str, method_name: str, *args: Any):
        layer_call = dict(method=method_name, args=args)
        self.add_call("applyCallToLayer", layer_id, layer_call)

    def add_layer(self, layer: LayerT | dict) -> None:
        if isinstance(layer, LayerT):
            layer = layer.model_dump()

        self.add_call("addLayer", layer)

    def remove_layer(self, layer_id: str) -> None:
        self.add_call("removeLayer", layer_id)

    def add_control(self, control: ControlT | dict) -> None:
        if isinstance(control, ControlT):
            control = control.model_dump()

        self.add_call("addControl", control)

    def remove_control(self, control_id: str) -> None:
        self.add_call("removeControl", control_id)

    def to_html(self, **kwargs) -> str:
        return HTMLTemplate().render(data=self.map_options, **kwargs)

    def save(self, path: Path | str = None, preview: bool = True, **kwargs) -> str:
        path = write_file(content=self.to_html(**kwargs), path=path)
        if preview:
            webbrowser.open(path)

        return path
