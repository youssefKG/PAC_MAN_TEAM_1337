from src.mlx.libmlx import (
    RendererType,
    new_image,
    image_to_window,
    put_pixel,
    Image
)
from .base import BaseImage, ImageType
from src.core.rgb_colors import RgbColors

class PixelImage(BaseImage):
    def __init__(
            self,
            /, 
            *,
            renderer: RendererType,
            width: int,
            height: int,
            image_type: ImageType,
            z_index: int,
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            z_index=z_index,
        )
        self.__image: Image = new_image(self._renderer, width, height)


    def to_window(self) -> None:
        image_to_window(
            self._renderer,
            self.__image, int(self._position.x),
            int(self._position.y)
        )

    def update(self, elapsed_time: float) -> None:
        self.__image.contents.instances[0].x = int(self._position.x)
        self.__image.contents.instances[0].y = int(self._position.y)

    def set_background_color(self, color: RgbColors) -> None:
        for y in range(self._height):
            for x in range(self._width):
                put_pixel(self.__image, x, y, color.value)
