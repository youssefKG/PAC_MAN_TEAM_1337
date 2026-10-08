from src.mlx.libmlx import (
    RendererType,
)
from src.core.vector2 import Vector2
from enum import Enum, auto
from typing import Protocol
import sys

class ImageType(Enum):
    FRAME_IMAGE = auto()
    PIXEL_IMAGE = auto()
    GRID_IMAGE = auto()
    PNG_IMAGE = auto()


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
            parent: 'BaseImage | None' = None
        ) -> None:
        self._renderer: RendererType = renderer
        self._width: int 
        self._height: int
        self.__set_dimensions(width=width, height=height, parent=parent)
        self.image_type: ImageType = image_type
        self.__z_index: int = z_index
        self._position: Vector2 = Vector2(x=0.0, y=0.0)
        self.parent: 'BaseImage | None' = parent
        self.set_parent(position if position is not None else (0, 0))

    def set_position(self, position: Vector2) -> None:
        self._position.add(position)

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

    def set_parent(self, coordinates: tuple[int | float, int | float]) -> None:
        current_image: BaseImage | None = self
        x, y = coordinates
        position: Vector2 = Vector2(x=x, y=y)
        if isinstance(x, int) and isinstance(y, int):
            while current_image:
                position.add(current_image.position)
                current_image = current_image.parent
            self._position = position
        elif isinstance(x, float) and isinstance(y, float):
            parent: "BaseImage | None"  = self.parent
            print("from float")
            if parent is None:
                window_width, window_height = (0, 0)
            else:
                print(parent.width, parent.height, x, y)
                self._position = Vector2(x=parent.width * x, y=parent.height * y)
                self._position.add(parent.position)
                print(self.position.x, self.position.y)
        else:
            print("invalid value: ", x, y)
            sys.exit(1)


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

    def __set_dimension(
            self,
            dim: float | int,
            parent_dim: int,

    ) -> int:
        if isinstance(dim, int):
            return dim
        else:
            return int(dim * parent_dim)
