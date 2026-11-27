from src.mazegenerator import MazeGenerator
from src.core import PixelImage, Engine, ImageType, GridImage, RgbColors, FrameImage, Vector2
import math

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
        self.__cell_size: int = self.__cell_dimension
        self.__cell_border_size: int = math.ceil(self.__cell_size * 0.10)
        self.__cell_content_size: int = self.__cell_size - (
            self.__cell_border_size * 2
        )
        self.__maze: PixelImage = self.__new_maze()
        self.__cells_42: list[tuple[int, int]] = self._cells_42()

    def __new_maze_background(self) -> PixelImage:
        maze_background: PixelImage = self.__engine.new_image(
                width=.76,
                height=.75,
                image_type=ImageType.PIXEL_IMAGE,
                position=(.493, .5)
        ).set_parent(self.__maze_wrapper).to_center().create()
        maze_background.set_background_color(RgbColors.TRANSPARENT_GREEN)
        return maze_background


    @property
    def cell_size(self) -> int:
        return self.__cell_border_size * 2 + self.__cell_content_size

    @property
    def cell_content_size(self) -> int:
        return self.__cell_content_size

    @property
    def maze(self) -> PixelImage:
        return self.__maze

    @property
    def cell_border_size(self) -> int:
        return self.__cell_border_size

    @property
    def vertical_cells(self) -> int:
        return self.__vertical_cells


    @property
    def horizontal_cells(self) -> int: 
        return self.__horizontal_cells

    def __new_maze(self) -> PixelImage:
        width: int = (self.__cell_border_size * 2 + self.__cell_content_size) * self.__horizontal_cells
        height: int = (self.__cell_border_size * 2 + self.__cell_content_size) * self.__vertical_cells
        maze: PixelImage = self.__engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=width,
            height=height,
            position=(.5, .5),
        ).set_parent(self.__maze_background).to_center().create()
        return maze

    def __new_maze_wrapper(self) -> GridImage:
        max_cells: int = max(self.__vertical_cells, self.__horizontal_cells)
        _, window_height = self.__engine.window_dimension
        width = int ((window_height * .7) / max_cells) * self.__horizontal_cells
        height = int ((window_height * .7) / max_cells) * self.__vertical_cells
        return self.__engine.new_image(
            image_type=ImageType.GRID_IMAGE,
            width=width,
            height=height,
            total_cols=5,
            total_rows=4,
            col=2,
            row=3,
            path="src/assests/menu/green_menu.png",
            position=(.5, .5)
        ).set_parent(self.__parent).to_center().create()

    @property
    def __cell_dimension(self) -> int:
        return self.__maze_background.height // self.__vertical_cells

    def draw(self) -> None:
        for row, cells_row in enumerate(self.__maze_generator.maze):
            for col, cell_hexa in enumerate(cells_row):
                self.__draw_cell(cell_hexa, row, col)

    def has_border(self, cell_hexa: int, direction: int) -> bool:
        return (cell_hexa & (1 << direction)) != 0


    @property
    def maze_hexa(self) -> list[list[int]]:
        return self.__maze_generator.maze

    @property
    def position(self) -> Vector2:
        return self.__maze.position

    def __draw_cell(self, cell_hexa: int, row: int, col: int) -> None:
        north: bool = self.has_border(cell_hexa, 0)
        east: bool  = self.has_border(cell_hexa, 1)
        south: bool = self.has_border(cell_hexa, 2)
        west: bool = self.has_border(cell_hexa, 3)
        start_x: int
        start_y: int
        end_x: int
        end_y: int
        cell_size: int = (self.__cell_border_size * 2) + self.__cell_content_size 
        if north:
            start_x = col * cell_size - self.__cell_border_size 
            start_y = row * cell_size - self.__cell_border_size

            end_x = start_x + cell_size + (self.__cell_border_size * 2)
            end_y = start_y + (self.__cell_border_size * 2)
            if col == 0:
                start_x += self.__cell_border_size
            if row == 0:
                start_y += self.__cell_border_size

            if col == self.__horizontal_cells - 1:
                end_x -= self.__cell_border_size

            self.__maze.np_put_pixel(start_x, end_x, start_y, end_y, RgbColors.GREEN)
        if east:
            start_x = col * cell_size + self.__cell_border_size + self.__cell_content_size 
            start_y = row * cell_size - self.__cell_border_size

            end_x = start_x + (self.__cell_border_size * 2)
            end_y = start_y + cell_size + (self.__cell_border_size * 2)

            if col == self.__horizontal_cells - 1:
                end_x -= self.__cell_border_size
            if row == 0:
                start_y += self.__cell_border_size
            if row == self.__vertical_cells - 1:
                end_y -= self.__cell_border_size

            self.__maze.np_put_pixel(start_x, end_x, start_y, end_y, RgbColors.GREEN)
        if south:
            start_x = col * cell_size
            start_y = row * cell_size + self.__cell_content_size + self.__cell_border_size

            end_x = start_x + cell_size
            end_y = start_y + (self.__cell_border_size * 2)
            if row == self.__vertical_cells - 1:
                end_y -= self.__cell_border_size
            if col == 0:
                start_x += self.__cell_border_size
            if col == self.__horizontal_cells -1:
                end_x -= self.__cell_border_size

            self.__maze.np_put_pixel(start_x, end_x, start_y, end_y, RgbColors.GREEN)
        if west:
            start_x = col * cell_size - self.__cell_border_size
            start_y = row * cell_size - self.__cell_border_size

            end_x = start_x + (self.__cell_border_size * 2)
            end_y = start_y + cell_size + (self.__cell_border_size * 2)

            if col == 0:
                start_x += self.__cell_border_size
            if row == 0:
               start_y += self.__cell_border_size 
            if row == self.__vertical_cells - 1:
                end_y -= self.__cell_border_size

            self.__maze.np_put_pixel(start_x, end_x, start_y, end_y, RgbColors.GREEN)
        if (row, col) in self.__cells_42:
            start_x = col * cell_size + self.__cell_border_size
            end_x = start_x + self.__cell_content_size
            start_y = row * cell_size + self.__cell_border_size
            end_y = start_y + self.__cell_content_size
            self.__maze.np_put_pixel(start_x, end_x, start_y, end_y, RgbColors.WHITE)

    def _cells_42(self) -> list[tuple[int, int]]:
        """Draw a “42” pattern in the maze for decoration."""
        y = int(((self.__vertical_cells) / 2) - 3)
        x = int(((self.__horizontal_cells) / 2) - 4)
        cells_42: list[tuple[int, int]] = list()

        for i in range(y, y + 3):
            cells_42.append((i, x))
        for i in range(x + 1, x + 3):
            cells_42.append((y + 2, i))
        for i in range(y + 3, y + 5):
            cells_42.append((i, x + 2))

        for i in range(x + 4, x + 7):
            cells_42.append((y, i))
        for i in range(y + 1, y + 3):
            cells_42.append((i, x + 6))
        for i in range(x + 4, x + 7):
            cells_42.append((y + 2, i))
        for i in range(y + 3, y + 5):
            cells_42.append((i, x + 4))
        for i in range(y + 3, y + 5):
            cells_42.append((i,x + 4))
        for i in range(x + 4, x + 7):
            cells_42.append((y + 4,i))
        return cells_42

