import os
from src.mlx.libmlx import (
    new_image,
    ImageType,
    RendererType,
    image_to_window,
    put_pixel,
    load_png,
    # texture_to_image,
    TextureType,
    get_frames_of_images,
    resize_image
)
from src.core.vector2 import Vector2
from typing import Protocol
from .base import BaseImage, ImageFormat
from ..rgb_colors import RgbColors
from pathlib import Path
import ctypes
from typing import cast




_DEFAULT_IMAGE_WIDTH = 100
_DEFAULT_IMAGE_HEIGHT = 100

class ImageInterface(Protocol):
    def set_position(self, position: Vector2) -> None:
        ...

    def to_window(self) -> None:
        ...

    def move(self, v: Vector2) -> None:
        ...

    def update(self, elapsed_time: float) -> None:
        ...

    @property
    def position(self) -> Vector2:
        ...

class FrameImage(BaseImage):
    def __init__(
            self,
            /, 
            *,
            renderer: RendererType,
            width: int,
            height: int,
            image_format: ImageFormat,
            path: str,
            time_per_frame: float,
            frames:  int = 1,
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_format=image_format
        )
        self._path: str = path
        self._frames: int = 1
        self.__texture_image: TextureType = load_png(
            "src/assests/orange_ghost.png"
        )
        self.__frames_image: list[ImageType] = get_frames_of_images(self._renderer, self.__texture_image, frames=8)
        self.__time_passed: float = 0.
        self.__current_frame_idx: int = 0
        self.__is_backwords: bool = False
        self.__time_per_frame: float = time_per_frame
        for image_frame in self.__frames_image:
            resize_image(image_frame, self._width, self._height)

    def image_to_window(self) -> None:
        image_to_window(
            self._renderer,
            self.__frames_image[self.__current_frame_idx], int(self._position.x),
            int(self._position.y)
        )

    def to_window(self) -> None:
        for frame_image in self.__frames_image:
            frame_image.contents.enabled = False
            image_to_window(
                self._renderer,
                frame_image,
                int(self._position.y),
                int(self._position.x)
            )

    @property
    def __get_current_image(self) -> ImageType:
        return self.__frames_image[self.__current_frame_idx]

    def move(self, v: Vector2) -> None:
        self._position.add(v)

    def update(self, elapsed_time: float) -> None:
        print(elapsed_time)
        current_image: ImageType = self.__get_current_image
        if self.__time_passed >= self.__time_per_frame:
            current_image.contents.enabled = False
            if self.__current_frame_idx == len(self.__frames_image) - 1:
                self.__current_frame_idx = 0
            self.__current_frame_idx += 1
            current_image = self.__get_current_image
            current_image.contents.enabled = True
            self.__time_passed -= self.__time_per_frame
        self.__time_passed += elapsed_time
        current_image.contents.instances[0].x = self._position.x
        current_image.contents.instances[0].y = self._position.y

    def move(self, vector: Vector2, dt: float) -> None:
        pass



class PixelImage(BaseImage):
    def __init__(
            self,
            /, 
            *,
            renderer: RendererType,
            width: int,
            height: int,
            image_format: ImageFormat
        ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_format=image_format
        )
        self.__image: ImageType = new_image(self._renderer, width, height)


    def to_window(self) -> None:
        image_to_window(
            self._renderer,
            self.__image, int(self._position.x),
            int(self._position.y)
        )

    def move(self, v: Vector2) -> None:
        self._position.add(v)

    def update(self, _: float) -> None:
        pass

    def update(self, elapsed_time: float) -> None:
        self.__image.contents.instances[0].x = int(self._position.x)
        self.__image.contents.instances[0].y = int(self._position.y)

    def set_background_color(self, color: RgbColors) -> None:
        for y in range(self._height):
            for x in range(self._width):
                put_pixel(self.__image, x, y, color.value)


class ImageFactory:
    def __init__(self, renderer: RendererType) -> None:
        self.__renderer: RendererType = renderer

    def __call__(self,
            image_format: ImageFormat=ImageFormat.PIXEL,
            width: int=_DEFAULT_IMAGE_WIDTH,
            height: int = _DEFAULT_IMAGE_HEIGHT,
            frames: int=1,
            path: str = "",
            time_per_frame: float = 0.
       ) -> ImageInterface:
        match image_format: 
            case ImageFormat.PNG:
                return  FrameImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_format=image_format,
                            frames=frames,
                            path=path,
                            time_per_frame=time_per_frame
                        )
            case ImageFormat.XPM:
                return  PixelImage(
                    renderer=self.__renderer,
                    width=width,
                    height=height,
                    image_format=image_format
                )
            case ImageFormat.PIXEL:
                return PixelImage(
                    renderer=self.__renderer,
                    width=width,
                    height=height,
                    image_format=image_format
                )
