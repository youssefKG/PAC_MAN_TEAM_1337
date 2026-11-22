from src.mlx.libmlx import (
    RendererType,
    new_image,
    Image,
    set_background_color,
    put_pixel,
    np_put_pixel
)
from typing_extensions import Self
from typing import override
from .base import BaseImage, ImageType
from src.core.rgb_colors import RgbColors

class PixelImage(BaseImage):
    def __init__(
            self,
            /, 
            *,
            renderer: RendererType,
            width: int | float,
            height: int | float,
            image_type: ImageType,
            position: tuple[int | float, int | float] | None,
            is_visible: bool,
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            position=position,
            is_visible=is_visible
        )

    @override
    def create(self) -> Self:
        self._image: Image = new_image(self._renderer, self._width, self._height)
        return self

    def set_background_color(self, color: RgbColors) -> None:
        set_background_color(self._image, color.value)

    def put_pixel(self, x: int, y: int, color: RgbColors) -> None:
        put_pixel(self._image, x, y, color.value)


    def np_put_pixel(self, start_x: int, end_x: int, start_y: int, end_y: int, color: RgbColors) -> None:
        np_put_pixel(
            self._image,
            self._width,
            self._height,
            start_x,
            end_x,
            start_y,
            end_y,
            color.value
        )
