from src.mlx.libmlx import (
    RendererType,
)
from src.core.vector2 import Vector2
from enum import Enum, auto

class ImageFormat(Enum):
    PNG = auto()
    XPM = auto()
    PIXEL = auto()

class BaseImage:
    def __init__(
            self,
            renderer: RendererType,
            width: int,
            height: int,
            image_format: ImageFormat
        ) -> None:
        self._renderer: RendererType = renderer
        self._width: int = width
        self._height: int = height
        self._position: Vector2 = Vector2(x=0., y=0.)
        self._image_format: ImageFormat = image_format

    def set_position(self, position: Vector2) -> None:
        self._position.add(position)

    @property
    def position(self) -> Vector2:
        return self._position
