from __future__ import annotations

import webbrowser
from pathlib import Path
from typing import Any

from .abstracts import LayerLike
from .export import HTMLTemplate, write_file
from .models.controls import ControlT
from .models.formats import GPX, KML, FormatT, GeoJSON, TopoJSON
from .models.layers import LayerT, TileLayer
from .models.map_options import MapOptions
from .models.sources import OSM, SourceT
from .models.view import View
from .styles import FlatStyle


class Map(object):
    """Initialize a new `Map` instance

    Args:
        view (View): The initial view state of the map
        layers (list[LayerT | LayerLike | dict]): Layers initially added to the map
        controls (list[ControlT | dict]): Controls initially added to the map
    """

    def __init__(
        self,
        view: View | dict = View(),
        layers: list[LayerT | LayerLike | dict] = None,
        controls: list[ControlT | dict] = None,
    ):
        self._initial_view_state = view.to_dict(exclude="type", exclude_none=True)
        self.calls = []
        if layers is None:
            layers = [TileLayer(id="osm", source=OSM())]

        self.options = MapOptions(
            view=view, layers=layers, controls=controls
        ).model_dump()

    @property
    def initial_view_state(self):
        return self._initial_view_state

    # 'apply_call_to_map'
    def add_call(self, method_name: str, *args: Any) -> None:
        call = dict(method=method_name, args=args)
        self.calls.append(call)

    # 'apply_call_to_layer'
    def add_layer_call(self, layer_id: str, method_name: str, *args: Any):
        layer_call = dict(method=method_name, args=args)
        self.add_call("applyCallToLayer", layer_id, layer_call)

    def add_view_call(self, method_name: str, *args: Any) -> None:
        view_call = dict(method=method_name, args=args)
        self.add_call("applyCallToView", view_call)

    def fit_bounds(self, bounds: tuple[float, float, float, float]) -> None:
        self.add_call("fitBounds", bounds)

    def set_view(self, view: View) -> None:
        """Set the view state of the map

        Args:
            view (View): The view state of the map
        """
        self.add_call("setView", view.model_dump())

    def set_view_from_source(self, layer_id: str) -> None:
        self.add_call("setViewFromSource", layer_id)

    def set_zoom(self, zoom_level: float | int) -> None:
        """Set the zoom level of the view

        Args:
            zoom_level (float | int): The zoom level
        """
        self.add_view_call("setZoom", zoom_level)

    def set_center(self, lon: float = 0, lat: float = 0) -> None:
        """Set the center of the view

        Args:
            lon (float): The center's longitude
            lat (float): The center's latitude
        """
        self.add_view_call("setCenter", (lon, lat))

    def add_layer(self, layer: LayerT | LayerLike | dict) -> None:
        """Add a layer to the map

        Args:
            layer (LayerT | LayerLike | dict): The layer to be added
        """
        if isinstance(layer, LayerLike):
            layer = layer.model

        if isinstance(layer, LayerT):
            layer = layer.model_dump()

        self.add_call("addLayer", layer)

    def remove_layer(self, layer_id: str) -> None:
        """Remove a layer from the map

        Args:
            layer_id (str): The ID of the layer to be removed
        """
        self.add_call("removeLayer", layer_id)

    def add_control(self, control: ControlT | dict) -> None:
        """Add a control to the map

        Args:
            control (ControlT | dict): The control to be added
        """
        if isinstance(control, ControlT):
            control = control.model_dump()

        self.add_call("addControl", control)

    def remove_control(self, control_id: str) -> None:
        """Remove a control from the map

        Args:
            control_id (str): The ID of the control to be removed
        """
        self.add_call("removeControl", control_id)

    def add_default_tooltip(self) -> None:
        """Add a default tooltip to the map

        It renders all feature properties
        and is activated for all layers of the map.
        """
        self.add_tooltip()

    def add_tooltip(self, template: str = None) -> None:
        """Add a tooltip to the map

        Args:
            template (str): A mustache template string.
                If `None`, a default tooltip is added to the map
        """
        self.add_call("addTooltip", template)

    def add_select_interaction(self) -> None:
        """Add `Select-Features` interaction to the map

        Note:
            Currently, highlighting selected features is not supported
            for layers of type `WebGLVectorLayer`.
        """
        self.add_call("addSelectFeatures")

    def add_drag_and_drop_interaction(
        self,
        formats: list[FormatT] = [GeoJSON(), TopoJSON(), GPX(), KML()],
        style: FlatStyle | dict = None,
    ) -> None:
        """Add a drag and drop interaction to the map"""
        formats = [f.model_dump() for f in formats]
        if isinstance(style, FlatStyle):
            style = style.model_dump()

        return self.add_call("addDragAndDropVectorLayers", formats, style)

    def add_click_interaction(self) -> None:
        """Add a click interaction to map"""
        self.add_call("addClickInteraction")

    def add_modify_interaction(self, layer_id) -> None:
        """Add a modify interaction to the map

        Modify features of a vector layer.

        Note:
            Layers of type `WebGLVectorLayer` are not supported.

        Args:
            layer_id (str): The ID of the layer you want to modify
        """
        return self.add_call("addModifyInteraction", layer_id)

    def set_opacity(self, layer_id: str, opacity: float = 1) -> None:
        """Set the opacity of a layer

        Args:
            layer_id (str): The ID of the layer
            opacity (float): The opacity of the layer. A value between 0 and 1
        """
        self.add_layer_call(layer_id, "setOpacity", opacity)

    def set_visibility(self, layer_id: str, visible: bool = False) -> None:
        """Set the visibility of a layer

        Args:
            layer_id (str): The ID of the layer
            visible (bool): Whether the layer is visible or not
        """
        self.add_layer_call(layer_id, "setVisible", visible)

    def set_style(self, layer_id: str, style: FlatStyle | dict) -> None:
        """Set the style of a layer

        Args:
            layer_id (str): The ID of the layer
            style (FlatStyle | dict): The style of the layer
        """
        if isinstance(style, FlatStyle):
            style = style.model_dump()

        self.add_layer_call(layer_id, "setStyle", style)

    def set_source(self, layer_id: str, source: SourceT | dict) -> None:
        """Set the source of a layer

        Args:
            layer_id {str}: The ID of the layer
            source (SourceT | dict): The source of the layer
        """
        if isinstance(source, SourceT):
            source = source.model_dump()

        self.add_call("setSource", layer_id, source)

    def to_html(self, **kwargs) -> str:
        """Render map to HTML"""
        data = self.options | dict(calls=self.calls)
        return HTMLTemplate().render(data=data, **kwargs)

    def save(self, path: Path | str = None, preview: bool = True, **kwargs) -> str:
        """Save map as an HTML document

        Args:
            path (Path | str): The Path to the output file. If `None`, a temporary file is created
            preview (bool): Whether the file should be opened in your default browser after saving
        """
        path = write_file(content=self.to_html(**kwargs), path=path)
        if preview:
            webbrowser.open(path)

        return path
