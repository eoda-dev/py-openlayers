# JupyterLite

```bash
uv sync
source .venv/bin/activate

jupyter lite build --contents contents --output-dir dist
cd dist
python -m http.server -d dist
```
