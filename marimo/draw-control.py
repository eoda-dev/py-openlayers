

import marimo

__generated_with = "0.13.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import openlayers as ol
    return mo, ol


@app.cell
def _(ol):
    m = ol.MapWidget(controls=[ol.DrawControl()])
    return (m,)


@app.cell
def _(m, mo):
    widget = mo.ui.anywidget(m)
    return (widget,)


@app.cell
def _(widget):
    widget
    return


@app.cell
def _(widget):
    widget.value["features"]
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
