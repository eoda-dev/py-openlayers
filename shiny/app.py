import json

from htmltools import h1
from shinywidgets import reactive_read, render_widget

import openlayers as ol
from shiny import reactive
from shiny.express import input, render, ui

city_centers = {
    "London": (51.5074, 0.1278),
    "Paris": (48.8566, 2.3522),
    "New York": (40.7128, -74.0060),
}

h1("python-openlayers")

ui.input_select("center", "Center", choices=list(city_centers.keys()))


@render_widget
def ol_map():
    lat, lon = city_centers["London"]
    m = ol.MapWidget(
        ol.View(center=(lon, lat), zoom=8),
        controls=[ol.OverviewMapControl(collapsed=False)],
    )
    return m


@render.code
def info():
    view_state = reactive_read(ol_map.widget, "view_state")
    return json.dumps(view_state, indent=2)


@reactive.effect
def _():
    lat, lon = city_centers[input.center()]
    ol_map.widget.set_center(lon, lat)
