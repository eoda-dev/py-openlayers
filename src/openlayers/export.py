from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from jinja2 import Template

from .templates import html_template

_CSS = Path(__file__).parent / "js" / "openlayers.standalone.css"
_JS = Path(__file__).parent / "js" / "openlayers.standalone.js"


def read_file(filename) -> str:
    with open(filename, "r") as f:
        content = f.read()

    return content


def write_file(content: str, path: Path | str = None) -> str:
    if path:
        with open(path, "w") as f:
            f.write(content)

        return path

    fd, path = tempfile.mkstemp(prefix="ol_")
    with os.fdopen(fd, "w") as tmp:
        tmp.write(content)

    return path


class HTMLTemplate(object):
    def __init__(
        self, template: str = None, css: Path | str = None, js: Path | str = None
    ) -> None:
        css = css or _CSS
        js = js or _JS
        self._template = template or html_template

        self._css = read_file(css) if os.path.isfile(css) else css
        self._js = read_file(js) if os.path.isfile(js) else js

    def render(self, data: dict = None, **kwargs) -> str:
        data = json.dumps(data or dict(viewOptions=dict(center=(0, 0))))
        headers = [f"<style>{self._css}</style>"]
        scripts = [self._js, f"var data={data}; renderOLMapWidget(data);"]
        return Template(self._template).render(
            headers=headers, scripts=scripts, js=self._js, **kwargs
        )
