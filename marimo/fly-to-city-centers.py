

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import openlayers as ol
    return mo, ol


@app.cell
def _():
    city_centers = {
        "London": (0.1278, 51.5074),
        "Paris": (2.3522, 48.8566),
        "New York": (-74.0060, 40.7128),
    }
    return (city_centers,)


@app.cell
def _():
    city = "London"
    return (city,)


@app.cell
def _(city, city_centers, ol):
    m = ol.MapWidget(ol.View(center=city_centers[city], zoom=8, projection="EPSG:4326"))
    return (m,)


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell(hide_code=True)
def _(city, city_centers, m, mo):
    mo.ui.dropdown(
        options=city_centers.keys(),
        label="City", value=city,
        # on_change=lambda key: m.add_view_call("animate", dict(center=city_centers[key], duration=2000))
        on_change=lambda key: m.set_center(*city_centers[key])
    )
    return


@app.cell
def _(widget):
    widget.value["view_state"]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
