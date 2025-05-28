

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import openlayers as ol
    from openlayers.sources import PMTilesVectorSource
    from openlayers.styles import default_style
    return PMTilesVectorSource, default_style, ol


@app.cell
def _():
    data = "https://r2-public.protomaps.com/protomaps-sample-datasets/nz-buildings-v3.pmtiles"
    return (data,)


@app.cell
def _(PMTilesVectorSource, data, default_style, ol):
    pmtiles = ol.layers.VectorTileLayer(
        id="pmtiles-vector",
        style=default_style(stroke_color="green", stroke_width=2),
        source=PMTilesVectorSource(
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
