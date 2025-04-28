

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import geopandas as gpd
    import openlayers as ol
    return gpd, mo, ol


@app.cell
def _():
    url = "https://openlayers.org/en/v4.6.5/examples/data/geojson/countries.geojson"
    return (url,)


@app.cell
def _(gpd, url):
    countries = gpd.read_file(url)
    return (countries,)


@app.cell
def _(countries, ol):
    m = countries.openlayers.explore(controls=[ol.json_defs.ScaleLineControl()], style={"fill-color": "green", "stroke-color": "yellow"})
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
def _(m):
    m.add_call("addTooltip", "name")
    # m.add_control(ol.json_defs.InfoBox(id="hi-there", html="Hi <b>there</b>", css_text="background: white;top:100px;"))
    # m.remove_control("hi-there");
    return


@app.cell
def _(ol):
    # m.add_control(ol.json_defs.MousePositionControl(id="mpc"))
    ol.json_defs.InfoBox(id="hi-there", html="Hi <b>there</b>", css_text="background: white;top:100px;").model_dump()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
