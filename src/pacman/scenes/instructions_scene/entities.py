from src.core import Engine, PixelImage, PngImage
from enum import Enum, auto
from .maze import Maze

class Direction(Enum):
    UP = 0
    DOWN = 2
    LEFT = 3
    RIGHT = 1

class Entity:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        size: int,
        position: tuple[int | float, int | float]
    ) -> None:
        self._engine: Engine = engine
        self._parent: PixelImage | PngImage = parent
        self._size: int = size
        self._position: tuple[int | float, int | float] = position


    def is_collide(self, entity: 'Entity') -> bool:
        _ = entity
        return False
