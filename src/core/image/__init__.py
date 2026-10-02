import os
from src.mlx.libmlx import (
    new_image,
    ImageType,
    RendererType,
    image_to_window,
    put_pixel,
    load_png,
    texture_to_image,
    TextureType
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

    def update(self) -> None:
        ...

    def set_background_color(self, color: RgbColors) -> None:
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
            "/home/totib/projects/PAC_MAN_TEAM_1337/src/assests/orange_ghost.png"
        )
        self.__image: ImageType = texture_to_image(self._renderer, self.__texture_image)
        self.__frames_image: list[ImageType] = list()
        self.__set_frames()


    def to_window(self) -> None:
        pass
        image_to_window(
            self._renderer,
            self.__image,
            int(self._position.y),
            int(self._position.x)
        )

    def __set_frames(self) -> None:
        width: int = cast(int, self.__texture_image.contents.width)
        height: int = cast(int, self.__texture_image.contents.height)
        width_per_frame: int = width // self._frames
        for frame_num in range(self._frames):
            frame_image: ImageType = new_image(
                self._renderer,
                width_per_frame,
                height,
            )
            print(len(ctypes.c_void_p(frame_image.contents.pixels)))

            start_x = frame_num * width_per_frame

            for y in range(height):
                for x in range(width_per_frame):
                    dst_offset = (y * width_per_frame + x) * 4
                    src_offset = (y * width + start_x + x) * 4

                    frame_image.contents.pixels.pixels.contents.value[dst_offset:dst_offset + 4] = (
                        self.__texture_image.contents.pixels.contents.value[
                            src_offset:src_offset + 4
                        ]
                    )

            self.__frames_image.append(frame_image)
    def move(self, v: Vector2) -> None:
        self._position.add(v)

    def update(self) -> None:
        pass
        # self.__image.contents.instances[0].x = int(self._position.x)
        # self.__image.contents.instances[0].y = int(self._position.y)

    def set_background_color(self, color: RgbColors) -> None:
        pass
        # for y in range(self._height):
        #     for x in range(self._width):
        #         put_pixel(self.__image, x, y, color.value)


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

    def update(self) -> None:
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
            path: str = ""
       ) -> ImageInterface:
        match image_format: 
            case ImageFormat.PNG:
                return  FrameImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_format=image_format,
                            frames=frames,
                            path=path
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

