from typing import cast
from src.core import Engine, GridImage, ImageType, PixelImage, FrameImage, RgbColors
from src.mazegenerator import MazeGenerator
from src.core import Vector2


class Maze:
    def __init__(
        self,
        parent: PixelImage,
        engine: Engine,
        vertical_cells: int,
        horizontal_cells: int,
        position: tuple[int | float, int | float],
        maze_generator: MazeGenerator,
    ) -> None:
        self.__engine: Engine = engine
        self.__vertical_cells: int = vertical_cells
        self.__horizontal_cells: int = horizontal_cells
        self.__position: tuple[int | float, int | float] = position
        self.__parent: PixelImage = parent
        self.__maze_generator: MazeGenerator = maze_generator
        self.__window_width, self.__window_height = self.__engine.window_dimension
        self.__maze_background_width, self.__maze_background_height = self.__get_background_dimensions
        self.__maze_wrapper: GridImage = cast(
            GridImage, 
            self.__engine.new_image(
                image_type=ImageType.GRID_IMAGE,
                width=self.__maze_background_width * self.__horizontal_cells,
                height=self.__maze_background_height * self.__vertical_cells,
                total_cols=5,
                total_rows=4,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=self.__position,
            )
            .set_parent(self.__parent)
            .to_center()
            .create()
        )
        self.__maze_background: PixelImage = cast(
            PixelImage,
            self.__engine.new_image(
                width=0.78,
                height=0.75,
                image_type=ImageType.PIXEL_IMAGE,
                position=(.5, .5)
            ).set_parent(self.__maze_wrapper)
            .to_center()
            .create()
        )
        self.__maze_background.set_background_color(RgbColors.TRANSPARENT_GREEN)
        self.__cell_width, self.__cell_height = self.__cell_dimension
        self.__cell_content_width, self.__cell_content_height = self.__cell_content_dimension(
            self.__cell_width,
            self.__cell_height
        )
        self.__pacman: FrameImage = cast(
            FrameImage,
            self.__engine.new_image(
                image_type=ImageType.FRAME_IMAGE,
                width=self.__cell_content_width,
                height=self.__cell_content_height,
                path="src/assests/frames/pacman.png",
                frames=8,
                position=(0., 0.),
                time_per_frame=.1,
            )
            .set_parent(self.__maze_background)
            .create()
        )
        self.draw_cell()


    @property
    def __get_background_dimensions(self) -> tuple[int, int]:
        max_cells: int = max(self.__vertical_cells, self.__horizontal_cells)
        return (
            int ((self.__window_height * 0.5) / max_cells),
            int ((self.__window_height * 0.5) / max_cells),
        )

    @property
    def __cell_dimension(self) -> tuple[int, int]:
        return (
            self.__maze_background.height // self.__vertical_cells,
            self.__maze_background.width // self.__horizontal_cells
        )

    def __cell_content_dimension(self, cell_width: int, cell_height: int) -> tuple[int, int]:
        return int(cell_width * 0.8), int(cell_height * 0.8)
    
    def draw_cell(self) -> None:
        for y in range(self.__cell_height):
            for x in range(self.__cell_width):
                self.__maze_background.put_pixel(x, y, RgbColors.PINK)


    @property
    def pacman_position(self) -> Vector2:
        return self.__pacman.position

    def update(self, elapsed_time: float) -> None:
        self.__pacman.update(elapsed_time)
