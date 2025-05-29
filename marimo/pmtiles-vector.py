

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
    mo.md(
        r"""
        # PMTiles vector source

        See also [pmtiles/openlayers](https://docs.protomaps.com/pmtiles/openlayers)
        """
    )
    return


@app.cell
def _():
    data = "https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles"
    return (data,)


@app.cell
def _(data, ol):
    pmtiles = ol.VectorTileLayer(
        id="pmtiles-vector",
        style=ol.FlatStyle(stroke_color="green", stroke_width=2),
        source=ol.PMTilesVectorSource(
            url=data, attributions=["© Land Information New Zealand"]
        ),
    )
    return (pmtiles,)


@app.cell
def _(ol):
    view = ol.View(center=(172.606201, -43.556510), zoom=12)
    return (view,)


@app.cell
def _(ol, pmtiles, view):
    m = ol.MapWidget(view, layers=[pmtiles])
    m.add_tooltip()
    return (m,)


@app.cell
def _(m):
    m
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
