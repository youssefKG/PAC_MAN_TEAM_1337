import sys
from typing_extensions import Self, Annotated

from src.mlx.libmlx import (
    Image,
    RendererType,
    image_to_window,
    image_from_bit_map,
    display_image,
    delete_image,
    hide_image
)
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
        line_spacing: int = 4,
     ) -> None:
        self.__text: str = text
        self.__font_size: int | float = font_size
        self.__lettere_spacing: int = lettere_spacing
        self.__characteres_images: list[tuple[Image | None, Annotated[str, "character"]]] = list()
        self.__line_spacing: int = line_spacing
        self.__renderer: RendererType = renderer
        self.__text_path: str = "src/assests/alpha/alpha.png"
        self.__position: Vector2 = Vector2(x=.0, y=.0)
        self.__color: RgbColors = color
        self.__set_characteres_images()
        self.__has_been_on_window = False

    def set_position(self, position: Vector2) -> None:
        self.__position = position

    @property
    def position(self) -> Vector2:
        return self.__position

    def __set_characteres_images(self) -> None:
        for ch in self.__text:
            if ch == '\n':
                self.__characteres_images.append((None, ch))
            elif ch not in CHARACTERES_BIT_MAP:
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
                self.__characteres_images.append((ch_image, ch))

    def mount(self) -> None:
        offset: int = int(self.__position.x)
        y: int = int(self.__position.y)
        if not self.__has_been_on_window:
            for idx, (image, ch) in enumerate(self.__characteres_images):
                if image:
                    image_to_window(
                        self.__renderer,
                        image,
                        offset,
                        int(y)
                    )
                    if idx != len(self.__characteres_images):
                        offset += self.__lettere_spacing
                    offset += int(self.__font_size)
                    self.__has_been_on_window = True
                elif ch == '\n':
                    y += int(self.__font_size) + self.__line_spacing
                    offset = int(self.__position.x)
        else:
            for  image, _ in self.__characteres_images:
                if image:
                    display_image(image)

    def unmount(self) -> None:
        for  image, _ in self.__characteres_images:
            if image:
                hide_image(image)

    def center_x(self) -> Self:
        text_width = len(self.__text) * (self.__font_size + (self.__lettere_spacing))
        self.__position.x -= text_width // 2
        return self

    def center_y(self) -> Self:
        self.__position.y -=  self.__font_size // 2
        return self

    def to_center(self) -> Self:
        return self.center_x().center_y()

    def delete(self) -> None:
        for image, _ in self.__characteres_images:
            if image:
                delete_image(self.__renderer, image)

__all__ = ["Text"]
