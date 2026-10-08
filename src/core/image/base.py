from src.mlx.libmlx import (
    RendererType,
)
from src.core.vector2 import Vector2
from enum import Enum, auto
from typing import Protocol

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
            position: Vector2 | None=None,
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
        self._position: Vector2 = position if position is not None else Vector2(x=.0, y=0.0)
        self.parent: 'BaseImage | None' = parent
        self.set_parent()

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

    def set_parent(self) -> None:
        current_image: BaseImage | None = self
        while current_image:
            self._position.add(current_image.position)
            current_image = current_image.parent


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
            dim: float | int | None,
            parent_dim: int,

    ) -> int:
        if dim is None:
            return 0
        elif isinstance(dim, int):
            return dim
        else:
            return int(dim * parent_dim)
