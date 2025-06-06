

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import openlayers as ol
    ol.__version__
    return mo, ol


@app.cell
def _():
    data = "https://maplibre.org/maplibre-gl-js/docs/assets/us_states.geojson"
    return (data,)


@app.cell
def _(data, ol):
    vector = ol.VectorLayer(
        # background="gray",
        source=ol.VectorSource(url=data),
        fit_bounds=True
    )
    return (vector,)


@app.cell
def _(ol, vector):
    m = ol.MapWidget(layers=[ol.basemaps.CartoBasemapLayer(), vector])
    m.add_tooltip()
    m.add_select_interaction()
    return (m,)


@app.cell
def _(m, mo):
    w = mo.ui.anywidget(m)
    return (w,)


@app.cell
def _(w):
    w
    return


@app.cell
def _(w):
    [feat["properties"] for feat in w.value["features"]["selected"] if w.value["features"]]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
