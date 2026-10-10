from src.mlx.libmlx import RendererType, Image, load_png_image, image_to_window
from .base import BaseImage, ImageType
from src.core.vector2 import Vector2
from typing_extensions import Self
from typing import override

class PngImage(BaseImage):
    def __init__(
            self,
             /,
             *,
            renderer: RendererType,
            width: int | float,
            height: int | float,
            image_type: ImageType,
            path: str,
            time_per_frame: float,
            position: tuple[int | float, int | float] | None=None,
            z_index: int = 1,
    ) -> None:
        super().__init__(
                renderer=renderer,
                width=width,
                height=height,
                image_type=image_type,
                position=position,
                z_index=z_index,
        )
        self.__path: str = path
        self.__image: Image
        self.__time_passed: float = 0.
        self.__time_per_frame: float = time_per_frame

    def to_window(self) -> None:
        image_to_window(self._renderer, self.__image, int(self._position.x), int(self._position.y))
        for text in self._texts:
            text.to_window()

    @override
    def create(self) -> Self:
        self.__image = load_png_image(
            renderer=self._renderer,
            path=self.__path,
            width=self._width,
            height=self._height
        )
        return self

    def update(self, elapsed_time: float) -> None:
        if self.__time_passed >= self.__time_per_frame:
            self.__time_passed -= self.__time_per_frame
            return
        self.__time_passed += elapsed_time
        self.__image.contents.instances[0].x = int(self._position.x)
        self.__image.contents.instances[0].y = int(self._position.y)
        
