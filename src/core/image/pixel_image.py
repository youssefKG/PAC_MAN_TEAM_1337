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
from src.core.event import EventHandler

class PixelImage(BaseImage):
    def __init__(
            self,
            /, 
            *,
            renderer: RendererType,
            event_handler: EventHandler,
            width: int | float,
            height: int | float,
            image_type: ImageType,
            position: tuple[int | float, int | float] | None,
            is_visible: bool,
        ) -> None:
        super().__init__(
            renderer=renderer,
            event_handler=event_handler,
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
