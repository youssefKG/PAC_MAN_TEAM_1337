from src.core import Engine, PixelImage, PngImage
from enum import Enum, auto
from .maze import Maze
from abc import ABC, abstractmethod

class Direction(Enum):
    UP = 0
    DOWN = 2
    LEFT = 3
    RIGHT = 1

class Entity(ABC):
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        size: int,
        position: tuple[int, int]
    ) -> None:
        self._engine: Engine = engine
        self._parent: PixelImage | PngImage = parent
        self._size: int = size
        self._position: tuple[int, int] = position


    def is_collide(self, entity: 'Entity') -> bool:
        x, y = self.position()
        entity_x, entity_y = entity.position()
        entity_size = entity.size
        if (
            x >= entity_x 
            and x < entity_x + entity_size 
            and y >= entity_y 
            and y < entity_y + entity_size
        ):
            return True
        return False

    @abstractmethod
    def position(self) -> tuple[int | float, int | float]:
        ...

    @property
    def size(self) -> int:
        return self._size
