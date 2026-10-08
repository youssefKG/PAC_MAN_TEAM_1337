from src.mlx.libmlx import (
    RendererType,
    new_image,
    image_to_window,
    put_pixel,
    Image,
    set_background_color
)
from src.core.vector2 import Vector2
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
            parent: BaseImage | None
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            z_index=z_index,
            position=position,
            parent=parent
        )
        self.__image: Image = new_image(self._renderer, self._width, self._height)
        print("background", self._position)

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
        set_background_color(self.__image, color.value, self._width, self._height)
