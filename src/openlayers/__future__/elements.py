from __future__ import annotations

from ..models.view import View as ViewModel


class View(object):
    def __init__(self, center: tuple[float, float], **kwargs) -> None:
        self._model = ViewModel(**(locals() | kwargs))

    def model_dump(self, **kwargs) -> dict:
        return self._model.model_dump(**kwargs)
