from typing import cast
from src.core import Engine, GridImage, ImageType, PixelImage

class Maze:
    def __init__(
        self,
        parent: PixelImage,
        engine: Engine,
        vertical_cells: int,
        horizontal_cells: int,
        width: int | float,
        height: int | float,
        position: tuple[int | float, int | float]
    ) -> None:
        self.__engine: Engine = engine
        self.__vertical_cells: int = vertical_cells
        self.__horizontal_cells: int = horizontal_cells
        self.__width: int | float  = width
        self.__height: int | float = height
        self.__position: tuple[int | float, int | float] = position
        self.__parent: PixelImage = parent
        self.__maze_wrapper: GridImage = cast(
            GridImage, 
            self.__engine.new_image(
                image_type=ImageType.GRID_IMAGE,
                width=self.__width,
                height=self.__height,
                total_cols=5,
                total_rows=4,
                col=0,
                row=0,
                path="src/assests/menu/green_menu.png",
                position=self.__position
            )
            .set_parent(self.__parent)
            .create()
        )
        self.__maze: PixelImage = cast(
            PixelImage, 
            self.__engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=1.,
                height=1.,
                position=(.5, .5),
            )
        )
