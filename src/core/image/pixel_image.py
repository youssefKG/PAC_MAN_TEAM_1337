from src.mlx.libmlx import (
    RendererType,
    new_image,
    image_to_window,
    Image,
    set_background_color
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
            z_index: int,
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            z_index=z_index,
            position=position,
        )

    @override
    def create(self) -> Self:
        self._image = new_image(self._renderer, self._width, self._height)
        return self

    def update(self, elapsed_time: float) -> None:
        self._image.contents.instances[0].x = int(self._position.x)
        self._image.contents.instances[0].y = int(self._position.y)

    def set_background_color(self, color: RgbColors) -> None:
        set_background_color(self._image, color.value)
