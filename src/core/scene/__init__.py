from typing_extensions import Self
from uuid import uuid4
from src.core.engine import Engine
from src.core.image import ImageInterface
from src.mlx.libmlx import RendererType
from abc import ABC

class Scene(ABC):
    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine
        self.__id = str(uuid4())

    @property
    def id(self) -> str:
        return self.__id

    def update(self, elapsed_time: float) -> None:
        pass
