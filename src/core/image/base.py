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
            width: int,
            height: int,
            image_type: ImageType,
            position: Vector2 | None=None,
            z_index: int = 1
        ) -> None:
        self._renderer: RendererType = renderer
        self._width: int = width
        self._height: int = height
        self._position: Vector2 = position if position is not None else Vector2(x=.0, y=0.0)
        self.image_type: ImageType = image_type
        self.__z_index: int = z_index

    def set_position(self, position: Vector2) -> None:
        self._position.add(position)

    def move_to(self, /, *,  target: Vector2, dt: float, speed_per_frame_unit: int=1) -> None:
        distance_vector: Vector2 = self._position.sub(target)
        distance_vector_normalized: Vector2 = distance_vector.normalize()
        velocity =  Vector2(
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
