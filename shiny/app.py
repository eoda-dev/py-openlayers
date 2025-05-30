import openlayers as ol
from shiny.express import render, ui, input
from shiny import reactive

from shinywidgets import render_widget, reactive_read

city_centers = {
    "London": (51.5074, 0.1278),
    "Paris": (48.8566, 2.3522),
    "New York": (40.7128, -74.0060)
}

ui.input_select("center", "Center", choices=list(city_centers.keys()))

@render_widget
def ol_map():
    lat, lon = city_centers["London"]
    m = ol.MapWidget()
    m.set_center(lon, lat)
    m.set_zoom(8)
    return m


@render.code
def info():
    view_state = reactive_read(ol_map.widget, "view_state")
    return str(view_state)

@reactive.effect
def _():
    lat, lon = city_centers[input.center()]
    ol_map.widget.set_center(lon, lat)