from __future__ import annotations

import webbrowser
from pathlib import Path
from typing import Any

from .abstracts import LayerLike
from .export import HTMLTemplate, write_file
from .models.controls import ControlT
from .models.layers import LayerT, TileLayer
from .models.map_options import MapOptions
from .models.sources import OSM
from .models.view import View
from .styles import FlatStyle


class Map(object):
    def __init__(
        self,
        view: View | dict = View(),
        layers: list[LayerT | LayerLike | dict] | None = None,
        controls: list[ControlT | dict] | None = None,
    ):
        self._initial_view = view
        self.calls = []
        if layers is None:
            layers = [TileLayer(id="osm", source=OSM())]

        # layers = [
        #    layer.model_dump() if isinstance(layer, LayerLike) else layer
        #    for layer in layers
        # ]
        self.map_options = MapOptions(
            view=view, layers=layers, controls=controls
        ).model_dump()

    @property
    def initial_view(self):
        return self._initial_view

    # 'apply_call_to_map'
    def add_call(self, method_name: str, *args: Any) -> None:
        call = dict(method=method_name, args=args)
        self.calls.append(call)

    # 'apply_call_to_layer'
    def add_layer_call(self, layer_id: str, method_name: str, *args: Any):
        layer_call = dict(method=method_name, args=args)
        self.add_call("applyCallToLayer", layer_id, layer_call)

    def add_layer(self, layer: LayerT | LayerLike | dict) -> None:
        if isinstance(layer, LayerLike):
            layer = layer.model

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

    def add_default_tooltip(self) -> None:
        self.add_tooltip()

    def add_tooltip(self, template: str | None = None) -> None:
        self.add_call("addTooltip", template)

    def set_opacity(self, layer_id: str, opacity: float = 1.0) -> None:
        self.add_layer_call(layer_id, "setOpacity", opacity)

    def set_visible(self, layer_id: str, visible: bool = False) -> None:
        self.add_layer_call(layer_id, "setVisible", visible)

    def set_layer_style(self, layer_id: str, style: dict | FlatStyle) -> None:
        if isinstance(style, FlatStyle):
            style = style.model_dump()

        self.add_layer_call(layer_id, "setStyle", style)

    def to_html(self, **kwargs) -> str:
        data = self.map_options | dict(calls=self.calls)
        return HTMLTemplate().render(data=data, **kwargs)

    def save(self, path: Path | str = None, preview: bool = True, **kwargs) -> str:
        path = write_file(content=self.to_html(**kwargs), path=path)
        if preview:
            webbrowser.open(path)

        return path
