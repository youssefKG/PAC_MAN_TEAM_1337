from src.core import PixelImage
from src.mazegenerator import MazeGenerator

class Cell:
    def __init__(self, cell_num: int, col: int, row: int, is_42: bool=False) -> None:
        self.__cell_num: int = cell_num
        self.__col: int = col
        self.__row: int = row
        self.__is_42: int = is_42



class Maze:
    def __init__(
        self,
        maze_generator: MazeGenerator,
        cell_width: int,
        cell_height: int,
        maze_wrapper: PixelImage
    ) -> None:
        self.__maze_generator: MazeGenerator = maze_generator
        self.__maze_wrapper: PixelImage = maze_wrapper
