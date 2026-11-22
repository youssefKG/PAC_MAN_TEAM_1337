from typing import cast
from src.mazegenerator import MazeGenerator
from src.core import PixelImage, Engine, ImageType, GridImage, RgbColors, FrameImage

class Maze:
    def __init__(
        self,
        engine: Engine,
        maze_generator: MazeGenerator,
        parent: PixelImage,
        vertical_cells: int,
        horizontal_cells: int
    ) -> None:
        self.__maze_generator: MazeGenerator = maze_generator
        self.__parent: PixelImage = parent
        self.__engine: Engine = engine
        self.__vertical_cells: int = vertical_cells
        self.__horizontal_cells: int =  horizontal_cells
        self.__maze_wrapper: GridImage = self.__new_maze_wrapper()
        self.__maze_background: PixelImage = self.__new_maze_background()
        self.__cell_size = self.__cell_dimension
        self.__cell_border_size: int = int(self.__cell_size * 0.3)
        self.__cell_content_size: int = int(self.__cell_size * 0.7)
        self.__pacman: FrameImage = cast(
            FrameImage,
            self.__engine.new_image(
                image_type=ImageType.FRAME_IMAGE,
                width=self.__cell_content_size,
                height=self.__cell_content_size,
                path="src/assests/frames/pacman.png",
                frames=8,
                position=(0., 0.),
                time_per_frame=.1,
            )
            .set_parent(self.__maze_background)
            .create()
        )

    @property
    def __background_dimension(self) -> tuple[int, int]:
        max_cells: int = max(self.__vertical_cells, self.__horizontal_cells)
        _, window_height = self.__engine.window_dimension
        return (
            int ((window_height * .5) / max_cells),
            int ((window_height * .5) / max_cells),
        )


    def __new_maze_background(self) -> PixelImage:
        maze_background: PixelImage = cast(
            PixelImage,
            self.__engine.new_image(
                width=.78,
                height=.75,
                image_type=ImageType.PIXEL_IMAGE,
                position=(.5, .5)
            ).set_parent(self.__maze_wrapper)
            .to_center()
            .create()
          )
        maze_background.set_background_color(RgbColors.WHITE)
        return maze_background

    def __new_maze_wrapper(self) -> GridImage:
        max_cells: int = max(self.__vertical_cells, self.__horizontal_cells)
        _, window_height = self.__engine.window_dimension
        width = int ((window_height * .6) / max_cells) * self.__horizontal_cells
        height = int ((window_height * .6) / max_cells) * self.__vertical_cells
        return cast(
            GridImage, 
            self.__engine.new_image(
                image_type=ImageType.GRID_IMAGE,
                width=width,
                height=height,
                total_cols=5,
                total_rows=4,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=(.65, .5)
            )
            .set_parent(self.__parent)
            .to_center()
            .create()
        )

    @property
    def __cell_dimension(self) -> int:
        return self.__maze_background.height // self.__vertical_cells

    def draw(self) -> None:
        for row, cells_row in enumerate(self.__maze_generator.maze):
            for col, cell_hexa in enumerate(cells_row):
                self.__draw_cell(cell_hexa, row, col)

    def __is_open(self, cell_hexa: int, direction: int) -> bool:
        return (cell_hexa & (1 << direction)) != 0


    def __draw_cell(self, cell_hexa: int, row: int, col: int) -> None:
        north: bool = self.__is_open(cell_hexa, 0)
        east: bool  = self.__is_open(cell_hexa, 1)
        south: bool = self.__is_open(cell_hexa, 2)
        west: bool = self.__is_open(cell_hexa, 3)
        print(north, south, east, west, cell_hexa)
        start_x: int
        start_y: int
        end_x: int
        end_y: int
        if north:
            start_x = col * self.__cell_size
            end_x = start_x + self.__cell_size

            start_y = row * self.__cell_size
            end_y = start_y + self.__cell_border_size

            self.__draw_border(start_x, end_x, start_y, end_y)
        if east:
            start_x = col * self.__cell_size + self.__cell_border_size + self.__cell_content_size
            end_x = start_x + self.__cell_border_size

            start_y = row * self.__cell_size
            end_y = start_y + self.__cell_size

            self.__draw_border(start_x, end_x, start_y, end_y)

        if south:
            start_x = col * self.__cell_size
            end_x = start_x + self.__cell_size

            start_y = row * self.__cell_size + self.__cell_content_size + self.__cell_border_size
            end_y = start_y + self.__cell_border_size

            self.__draw_border(start_x, end_x, start_y, end_y)
        if west:
            start_x = col * self.__cell_size
            end_x = start_x + self.__cell_border_size

            start_y = row * self.__cell_size
            end_y = start_y + self.__cell_size
            self.__draw_border(start_x, end_x, start_y, end_y)


    def update(self, elapsed_time: float) -> None:
        self.__pacman.update(elapsed_time)
        pass

    def __draw_border(
        self,
        start_x: int ,
        end_x: int,
        start_y: int,
        end_y: int
    ) -> None:
        for y in range(start_y, end_y):
            for x in range(start_x, end_x):
                self.__maze_background.put_pixel(
                    x,
                    y,
                    RgbColors.GREEN
                )
