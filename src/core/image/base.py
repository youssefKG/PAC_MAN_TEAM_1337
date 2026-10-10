import sys
from typing import Protocol
from typing_extensions import Self
from enum import Enum, auto
from src.mlx.libmlx import (
    RendererType,
    get_monitor_size
)
from src.core.vector2 import Vector2
from src.utils import Logger
from src.core.text import Text

class ImageType(Enum):
    FRAME_IMAGE = auto()
    PIXEL_IMAGE = auto()
    GRID_IMAGE = auto()
    PNG_IMAGE = auto()

class Position(Enum):
    CENTER = auto()
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()




class ImageInterface(Protocol):
    def set_position(self, position: Vector2) -> None:
        ...

    def to_window(self) -> None:
        ...

    def move_to(self, /, *,  target: Vector2, dt: float, speed_per_frame_unit: int=1) -> None:
        ...

    def update(self, elapsed_time: float) -> None:
        ...

    @property
    def position(self) -> Vector2:
        ...

class BaseImage:
    def __init__(
            self,
            /,
            *,
            renderer: RendererType,
            width: int | float,
            height: int | float,
            image_type: ImageType,
            position: tuple[int | float, int | float] | None=None,
            top: int = 0,
            right: int = 0,
            left: int = 0,
            bottom: int = 0,
            z_index: int = 1,
        ) -> None:
        self._renderer: RendererType = renderer
        self.__temp_width: int | float = width
        self.__temp_height: int | float = height
        self.__temp_position: tuple[int | float, int | float] | None= position
        self._width: int 
        self._height: int
        self.image_type: ImageType = image_type
        self.__z_index: int = z_index
        self._position: Vector2 = Vector2(x=0.0, y=0.0)
        self._parent: 'BaseImage | None' = None
        self._texts: list[Text] = list()

    def set_position(self, position: Vector2) -> None:
        self._position.add(position)

    def set_parent(self, parent: 'BaseImage | None'=None) -> Self:
        self._parent = parent
        self.__set_dimensions(width=self.__temp_width, height=self.__temp_height, parent=parent)
        self.__init_position(self.__temp_position if self.__temp_position is not None else (0, 0))
        return self

    def move_to(self, /, *,  target: Vector2, dt: float, speed_per_frame_unit: int=1) -> None:
        distance_vector: Vector2 = self._position.sub(target)
        distance_vector_normalized: Vector2 = distance_vector.normalize()
        velocity = Vector2(
            x=distance_vector_normalized.x * speed_per_frame_unit,
            y=distance_vector_normalized.y * speed_per_frame_unit
        )
        self._position.move_to(
            Vector2(
                x=self._position.x + velocity.x * dt,
                y=self._position.y + velocity.y * dt,
            )
        )

    @property
    def position(self) -> Vector2:
        return self._position

    @property
    def z_index(self) -> int:
        return self.__z_index

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def __init_position(self, coordinates: tuple[int | float, int | float]) -> None:
        x, y = coordinates
        position: Vector2 = Vector2(x=x, y=y)
        parent: BaseImage | None = self._parent
        if isinstance(x, int) and isinstance(y, int):
            if parent is not None:
                position.add(parent.position)
            self._position = position
        elif isinstance(x, float) and isinstance(y, float):
            if parent is None:
                window_width, window_height = get_monitor_size()
                self._position = Vector2(x=window_width * x, y=window_height  * y)
            else:
                self._position = Vector2(x=parent.width * x, y=parent.height * y)
                self._position.add(parent.position)
        else:
            Logger.error(f"invalid coordinates: {x}, {y}", "Position Setter in base Image")
            sys.exit(1)

    def to_center(self) -> Self:
        self._position.add(Vector2(x=-(0.5 * self._width), y=-(0.5 * self._height)))
        return self

    def add_text(self, text: Text, position: tuple[int | float, int | float]) -> None:
        x, y = position
        if isinstance(x, int) and isinstance(y, int):
            text.position.add(Vector2(x=self._position.x, y=self._position.y))
        elif isinstance(x, float) and isinstance(y, float):
            text.position.add(Vector2(x=self._width * x,  y=self._height * y))
            text.position.add(self._position)
        else:
            Logger.error("invalide coordinates ({x}, {y})", __name__)
            sys.exit(1)
        self._texts.append(text)

    def __set_dimensions(
        self,
        *,
        width: float | int ,
        height: float | int,
        parent: 'BaseImage | None'
   ) -> None:
        parent_width: int = 0 if parent is None else parent.width
        parent_height: int = 0 if parent is None else parent.height
        self._width = self.__set_dimension(width, parent_width)
        self._height = self.__set_dimension(height, parent_height)

    def create(self) -> Self:
        return self

    def __set_dimension(
            self,
            dim: float | int,
            parent_dim: int,

    ) -> int:
        if isinstance(dim, int):
            return dim
        else:
            return int(dim * parent_dim)
