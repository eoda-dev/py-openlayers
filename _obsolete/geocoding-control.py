

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import openlayers as ol
    return mo, ol


@app.cell(hide_code=True)
def _(mo):
    mo.md("""You must set your __MapTiler API key__ to use the geocoding control""")
    return


@app.cell
def _():
    import os

    os.environ["MAPTILER_API_KEY"] = ""
    return (os,)


@app.cell
def _(ol):
    m = ol.MapWidget()
    return (m,)


@app.cell
def _(m, ol, os):
    if os.environ["MAPTILER_API_KEY"]:
        m.add_control(ol.MapTilerGeocodingControl(api_key=os.environ["MAPTILER_API_KEY"]))
    return


@app.cell
def _(m):
    m
    return


@app.cell
def _(ol):
    ol.constants.MAPTILER_API_KEY_ENV_VAR
    return


@app.cell
def _(ol, os):
    os.environ[ol.constants.MAPTILER_API_KEY_ENV_VAR]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
