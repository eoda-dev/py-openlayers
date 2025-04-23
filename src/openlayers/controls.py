from typing import Literal

from .abstracts import BaseType


class Control(BaseType): ...


class FullScreenControl(Control): ...


class ScaleLineControl(Control):
    bar: bool = False
    steps: int | None = None
    units: Literal["metric", "degrees", "imperial", "us", "nautical"] | None = None
    text: bool = False
