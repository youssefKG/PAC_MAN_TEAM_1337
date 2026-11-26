from src.core import Engine, FrameImage, ImageType, PixelImage, PngImage, Vector2, Key
from .entities import Entity, Direction
from .maze import Maze
from enum import Enum
import math


class Wall(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Pacman(Entity): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int | float, int | float],
        size: int,
        speed: int=80,
        maze: Maze,
    ) -> None:
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position,
        )
        self._pacman: FrameImage = self.__new_pacman()
        self.__direction: Direction | None = None
        self.__maze = maze
        self.__elapsed_time: float
        self.__speed: int = speed

    def __new_pacman(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=int(self._size* 0.8),
            height=int(self._size * .8),
            path="src/assests/frames/pacman.png",
            time_per_frame=.1,
            position=self._position,
            frames=8,
        ).set_parent(self._parent).create()


    def update(self, elapsed_time: float) -> None:
        self.__elapsed_time = elapsed_time
        match self.__direction:
            case Direction.UP:
                self.__move_up(elapsed_time)
            case Direction.DOWN:
                self.__move_down(elapsed_time)
            case Direction.LEFT:
                self.__move_left(elapsed_time)
            case Direction.RIGHT:
                self.__move_right(elapsed_time)
            case None:
                ...
        self._pacman.update(elapsed_time)

    def change_direction(self, new_direction: Direction) -> None:
        x, y = self._position
        col = int(x / self.__maze.cell_size)
        row = int(y / self.__maze.cell_size)
        has_border: bool = self.__maze.has_border(self.__maze.maze_hexa[row][col], new_direction.value)
        cell_x, cell_y = (
            col * self.__maze.cell_size + self.__maze.cell_border_size,
            row * self.__maze.cell_size + self.__maze.cell_border_size
        )
        x += self.__speed * self.__elapsed_time
        y += self.__speed * self.__elapsed_time
        print(cell_x, x, cell_y, y)
        distance: float = int(math.sqrt((x - cell_x) ** 2 + (y - cell_y) ** 2))
        print(distance)
        if has_border or distance > 20:
            return 
                
        self.__direction = new_direction

    def __move_up(self, elapsed_time: float) -> None:
        x, y = self._position
        col = int(x / self.__maze.cell_size)
        row = int((y - self.__maze.cell_border_size - self.__speed * elapsed_time + self.__maze.cell_size) / self.__maze.cell_size)
        if (
            row >= 0
            and not self.__maze.has_border(self.__maze.maze_hexa[row][col], 0)
        ):
            x, y = self._position
            self._position = x , y - self.__speed * elapsed_time
            self._pacman.position.add(x=.0, y=-self.__speed * elapsed_time)

    def __move_down(self, elapsed_time: float) -> None:
        x, y = self._position
        col = int(x / self.__maze.cell_size)
        row = int((y - self.__maze.cell_border_size + self.__speed * elapsed_time) / self.__maze.cell_size)
        if (
            row < self.__maze.vertical_cells 
            and not self.__maze.has_border(self.__maze.maze_hexa[row][col], 2)
        ):
            self._pacman.position.add(x=.0, y=self.__speed * elapsed_time)
            x, y = self._position
            self._position = x, y + self.__speed * elapsed_time

    def __move_left(self, elapsed_time: float) -> None:
        x, y = self._position
        col = int((x - self.__maze.cell_border_size - self.__speed * elapsed_time + self.__maze.cell_size) / self.__maze.cell_size)
        row = int(y / self.__maze.cell_size)
        if (
            col >= 0
            and not self.__maze.has_border(self.__maze.maze_hexa[row][col], 3)
        ):
            x, y = self._position
            self._position = x - self.__speed * elapsed_time, y
            self._pacman.position.add(x=-self.__speed * elapsed_time, y=.0)

    def __move_right(self, elapsed_time: float) -> None:
        x, y = self._position
        col = int((x - self.__maze.cell_border_size + self.__speed * elapsed_time) / self.__maze.cell_size)
        row = int(y / self.__maze.cell_size)
        if (
            col < self.__maze.horizontal_cells 
            and not self.__maze.has_border(self.__maze.maze_hexa[row][col], Wall.EAST.value)
        ):
            x, y = self._position
            self._position = x + self.__speed * elapsed_time, y
            self._pacman.position.add(x=self.__speed * elapsed_time, y=.0)

    def position(self) -> Vector2:
        return self._pacman.position
