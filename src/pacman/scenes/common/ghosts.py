import math
from .entity import Entity
from src.core import Engine, FrameImage, ImageType, PixelImage, PngImage, Vector2
from .maze import Maze
from .entity import Direction
from .pacman import Wall


class __Ghost(Entity):
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int | float, int | float],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position,
        )
        self._path: str
        self._ghost: FrameImage = self.__new_ghost()
        self._maze: Maze = maze
        
        self.__direction: Direction | None
        self.__next_direction: Direction | None = None

    def __new_ghost(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=self._size,
            height=self._size,
            path=self._path,
            time_per_frame=.1,
            position=self._position,
            frames=8
        ).set_parent(self._parent).create()

    def update(self, elapsed_time: float) -> None:
        # TODO: make the step dynamic
        step: int = int(self._maze.cell_size * elapsed_time) + 1
        ghost_position = int(self._ghost.position.x - self._parent.position.x), int(self._ghost.position.y - self._parent.position.y)
        x, y = ghost_position
        col = int(x / self._maze.cell_size)
        row = int(y / self._maze.cell_size)
        self.__can_switch_direction(ghost_position, col, row)
        match self.__direction:
            case Direction.UP:
                self.__move_up(step, ghost_position, col, row)
            case Direction.DOWN:
                self.__move_down(step, ghost_position, col, row)
            case Direction.LEFT:
                self.__move_left(step, ghost_position, col, row)
            case Direction.RIGHT:
                self.__move_right(step, ghost_position, col, row)
            case None:
                ...
        self._ghost.update(elapsed_time)

    def change_direction(self, new_direction: Direction) -> None:
        self.__next_direction = new_direction

    def __can_switch_direction(self, pacman_position: tuple[int, int], col: int, row: int) -> None:
        x, y = pacman_position
        if self.__next_direction is None or self.__next_direction == self.__direction:
            return
        has_border: bool = self._maze.has_border(
            self._maze.maze_hexa[row][col],
            self.__next_direction.value
        )
        if has_border:
            return
        cell_x, cell_y = (
            col * self._maze.cell_size + self._maze.cell_border_size,
            row * self._maze.cell_size + self._maze.cell_border_size,
        )
        distance: float = math.dist((int(x), int(y)), (int(cell_x), int(cell_y)))
        if int(distance) <= int(self._maze.cell_size * 0.2):
            self.__direction = self.__next_direction
            self._ghost.position.add(x=cell_x - x, y=cell_y - y)

    def __move_up(self, step: int, ghost_position: tuple[int, int], col: int, row: int) -> None:
        _, y = ghost_position 
        next_y = y - step
        north_border_y = row * self._maze.cell_size + self._maze.cell_border_size
        has_north_wall = self._maze.has_border(
            self._maze.maze_hexa[row][col],
            Wall.NORTH.value
        )
        if not has_north_wall or next_y >= north_border_y:
            self._ghost.position.y -= step

    def __move_down(self, step: int, pacman_position: tuple[int, int], col: int, row: int) -> None:
        _, y = pacman_position
        has_south_border: bool = self._maze.has_border(
            self._maze.maze_hexa[row][col],
            Wall.SOUTH.value
        )
        south_wall_y = row * self._maze.cell_size + self._maze.cell_content_size + self._maze.cell_border_size
        next_y = y + self._maze.cell_content_size + step
        if not has_south_border or  next_y <= south_wall_y:
            self._ghost.position.y += step

    def __move_left(self, step: int, pacman_position: tuple[int, int], col: int, row: int) -> None:
        x, _ = pacman_position
        has_south_border: bool = self._maze.has_border(
            self._maze.maze_hexa[row][col],
            Wall.WEST.value
        )
        west_wall_x = col * self._maze.cell_size + self._maze.cell_border_size
        next_x = x - step
        if not has_south_border or  next_x > west_wall_x:
            self._ghost.position.x -= step

    def __move_right(self, step: int, pacman_position: tuple[int, int], col: int, row: int) -> None:
        x, _ = pacman_position
        has_south_border: bool = self._maze.has_border(
                self._maze.maze_hexa[row][col],
                Wall.EAST.value
        )
        east_wall_x = col * self._maze.cell_size + self._maze.cell_border_size
        next_x = x + step
        if not has_south_border or  next_x < east_wall_x:
            self._ghost.position.x += step

    def position(self) -> Vector2:
        return self._ghost.position


class Clyde(__Ghost): 
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
        self._path: str = "src/assests/frames/blinky.png"
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position,
            speed=speed,
            maze=maze
        )
        # self.__direction: Direction | None = None
        self.__speed: int = speed
        self.__next_direction: Direction | None = None

    def chnage_direction(self, new_direction: Direction) -> None:
        self.__next_direction = new_direction


class Blinky(__Ghost): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int | float, int | float],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        self._path: str = "src/assests/frames/blinky.png"
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position,
            speed=speed,
            maze=maze
        )
        # self.__direction: Direction | None = None
        self.__speed: int = speed


class Pinky(__Ghost): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int | float, int | float],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        self._path: str = "src/assests/frames/blinky.png"
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position,
            speed=speed,
            maze=maze
        )
        # self.__direction: Direction | None = None
        self.__speed: int = speed
