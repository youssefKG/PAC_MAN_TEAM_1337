import sys
from typing import TypeAlias, Annotated
from typing_extensions import Self
from src.mlx.libmlx import Image, RendererType, image_to_window, image_from_bit_map, new_image, set_background_color

from .characteres_bit_map import CHARACTERES_BIT_MAP
from src.core.rgb_colors import RgbColors
from src.core.vector2 import Vector2
from src.utils import Logger

class Text:
    def __init__(
            self,
            /,
            *,
            renderer: RendererType,
            text: str,
            font_size: int | float,
            lettere_spacing: int,
            color: RgbColors,
     ) -> None:
        self.__text: str = text
        self.__font_size: int | float = font_size
        self.__lettere_spacing: int = lettere_spacing
        self.__characteres_images: list[Image] = list()
        self.__renderer: RendererType = renderer
        self.__text_path: str = "src/assests/alpha/alpha.png"
        self.__position: Vector2 = Vector2(x=.0, y=.0)
        self.__color: RgbColors = color
        self.__set_characteres_images()

    def set_position(self, position: Vector2) -> None:
        self.__position = position

    @property
    def position(self) -> Vector2:
        return self.__position

    def __set_characteres_images(self) -> None:
        for ch in self.__text:
            if ch not in CHARACTERES_BIT_MAP:
                Logger.error(f"Cannot find bit map for charatere {ch}", __name__)
                sys.exit(1)
            else:
                ch_bit_map: list[list[int]] = CHARACTERES_BIT_MAP[ch]
                ch_image: Image = image_from_bit_map(
                    self.__renderer,
                    ch_bit_map,
                    int(self.__font_size),
                    int(self.__font_size),
                    self.__color.value
                )
                self.__characteres_images.append(ch_image)

    def to_window(self) -> None:
        offset: int = int(self.__position.x)
        for idx, image in enumerate(self.__characteres_images):
            image_to_window(
                self.__renderer,
                image,
                offset,
                int(self.__position.y)
            )
            if idx != len(self.__characteres_images):
                offset += self.__lettere_spacing
            offset += int(self.__font_size)

    def center_x(self) -> Self:
        text_width = len(self.__text) * (self.__font_size + (self.__lettere_spacing))
        self.__position.x -= text_width // 2
        return self

    def center_y(self) -> Self:
        self.__position.y -=  self.__font_size // 2
        return self

    def to_center(self) -> Self:
        self.__position.y -=  self.__font_size // 2
        text_width = len(self.__text) * (self.__font_size + (self.__lettere_spacing))
        self.__position.x -= text_width // 2
        return self

__all__ = ["Text"]
