from .abstracts import MyBaseModel


class View(MyBaseModel):
    center: tuple[float, float] = (0, 0)
    zoom: float = 0
