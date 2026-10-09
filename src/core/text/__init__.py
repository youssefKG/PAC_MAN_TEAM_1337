import sys
from typing import TypeAlias, Annotated
from src.mlx.libmlx import Image, get_image_from_grid_texture, RendererType, image_to_window
from src.core.vector2 import Vector2
from src.utils import Logger




CharPosition: TypeAlias = dict[str, tuple[Annotated[int, "row"], Annotated[int, "col"]]]


characters_position: CharPosition =  {
        "0": (1, 0),
        "1": (1, 1),
        "2": (1, 2),
        "3": (1, 3),
        "4": (1, 4),
        "5": (1, 5),
        "6": (1, 6),
        "7": (1, 7),
        "8": (1, 8),
        "9": (1, 9),
}

class Text:
    def __init__(
            self,
            /,
            *,
            renderer: RendererType,
            text: str,
            font_size: int | float,
            lettere_spacing: int
     ) -> None:
        self.__text: str = text
        self.__font_size: int | float = font_size
        self.__lettere_spacing: int = lettere_spacing
        self.__characteres_images: list[Image] = list()
        self.__renderer: RendererType = renderer
        self.__text_path: str = "src/assests/alpha/alpha.png"
        self.__position: Vector2
        self.__set_characteres_images()

    def set_position(self, position: Vector2) -> None:
        self.__position = position

    @property
    def position(self) -> Vector2:
        return self.__position

    def __set_characteres_images(self) -> None:
        for ch in self.__text:
            if ch not in characters_position:
                Logger.error("Cannot find the carachtere {ch}", __name__)
                sys.exit(1)
            row, col = characters_position[ch]
            print(row, col, ch)
            image: Image = get_image_from_grid_texture(
                renderer=self.__renderer,
                total_rows=6,
                total_cols=16,
                row=row,
                col=col,
                path=self.__text_path,
                width=int(self.__font_size),
                height=int(self.__font_size)
            )
            self.__characteres_images.append(image)

    def to_window(self) -> None:
        for idx, image in enumerate(self.__characteres_images):
            image_to_window(
                self.__renderer,
                image,
                int(idx  * self.__font_size + self.__position.x),
                int(self.__position.y)
            )
            # if idx != len(self.__characteres_images) - 1:
            #     offset += self.__lettere_spacing

__all__ = ["Text"]
