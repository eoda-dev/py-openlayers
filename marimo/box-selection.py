

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import openlayers as ol
    import marimo as mo
    return mo, ol


@app.cell
def _(ol):
    layer = ol.VectorLayer(
        source=ol.sources.VectorSource(
            url="https://openlayers.org/data/vector/ecoregions.json"
        )
    )
    return (layer,)


@app.cell
def _(layer, ol):
    m = ol.MapWidget(layers=[layer])
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
    w.value["view_state"]
    return


@app.cell
def _(m):
    m.add_call("addBoxSelection")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
