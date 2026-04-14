

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
    data = "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson"
    # data = "https://github.com/visgl/deck.gl-data/raw/master/examples/line/airports.json"
    layer = ol.WebGLVectorLayer(
        id="xyz",
        source=ol.sources.VectorSource(
            url=data,
            # url="https://openlayers.org/data/vector/ecoregions.json"
            crossOrigin="anonymous"

        ),
        style=ol.FlatStyle(
            circle_radius=5,
            circle_fill_color="red", circle_stroke_color="green")
    )
    return (layer,)


@app.cell
def _(layer, ol):
    m = ol.MapWidget(layers=[ol.BasemapLayer(), layer])
    # m.add_layer(layer)
    return (m,)


@app.cell
def _(m, mo):
    w = mo.ui.anywidget(m)
    return (w,)


@app.cell
def _():
    return


@app.cell
def _(w):
    w
    return


@app.cell
def _():
    # w.value["view_state"]
    return


@app.cell
def _(m):
    m.add_call("addBoxSelection")
    return


@app.cell
def _(m):
    m.add_select_interaction()
    return


@app.cell
def _(w):
    w.value["features"]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
