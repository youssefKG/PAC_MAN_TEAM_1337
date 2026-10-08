from typing import override
from src.mlx.libmlx import RendererType, get_image_from_grid_texture, Image, image_to_window
from .base import BaseImage, ImageType
from src.core.vector2 import Vector2

class GridImage(BaseImage):
    def __init__(
        self,
        /,
        *,
        renderer: RendererType,
        width: int | float,
        height: int | float,
        image_type: ImageType,
        position: Vector2 | None=None,
        total_cols: int,
        total_rows: int,
        col: int,
        row: int,
        path: str,
        z_index: int = 1,
        parent: BaseImage | None,
    ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            position=position,
            z_index=z_index,
            parent=parent
        )
        self.__total_rows: int = total_rows
        self.__total_cols: int = total_cols
        self.__row: int = row
        self.__col: int = col
        self.__image: Image = get_image_from_grid_texture(
            renderer=self._renderer,
            path=path,
            col=self.__col,
            row=self.__row,
            total_cols=self.__total_cols,
            total_rows=self.__total_rows,
            width=self._width,
            height=self._height
        )


    def to_window(self) -> None:
        image_to_window(
            self._renderer,
            self.__image,
            int(self._position.x),
            int(self._position.y)
        )

    @override
    def move_to(self, /, *, target: Vector2, dt: float, speed_per_frame_unit: int=1) -> None:
        pass

    def update(self, elapsed_time: float) -> None:
        ...
