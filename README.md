# OpenLayers for Python

[![Release](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)](https://img.shields.io/github/v/release/eoda-dev/py-openlayers)
[![pypi](https://img.shields.io/pypi/v/openlayers.svg)](https://pypi.python.org/pypi/openlayers)
[![License](https://img.shields.io/github/license/eoda-dev/py-openlayers)](https://img.shields.io/github/license/eoda-dev/py-openlayers)
[![OpenLayers JS](https://img.shields.io/badge/OpenLayers-v10.5.0-blue.svg)](https://github.com/openlayers/openlayers/releases//tag/v10.5.0)

## Installation

```bash
uv init

uv add "git+https://github.com/eoda-dev/py-openlayers@main"
```

## Quickstart

```python
import openlayers as ol

# Jupyter or Marimo
ol.MapWidget()

# Standalone
m = ol.Map()
m.save()
```
