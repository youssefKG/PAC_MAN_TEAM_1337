from typing import override
from .entities import Entity
from src.core import Engine, FrameImage, ImageType, PixelImage, PngImage
from .maze import Maze

class __Ghost(Entity):
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int, int],
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
        self._ghost.update(elapsed_time)

    @override
    def position(self) -> tuple[int | float, int | float]:
        return self._ghost.position.x, self._ghost.position.y

class Clyde(__Ghost): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int, int],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        self._path = "src/assests/frames/clyde.png"
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

    @override
    def position(self) -> tuple[int | float, int | float]:
        return self._ghost.position.x, self._ghost.position.y

class Blinky(__Ghost): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int, int],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        self._path = "src/assests/frames/blinky.png"
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

    @override
    def position(self) -> tuple[int | float, int | float]:
        return self._ghost.position.x, self._ghost.position.y


class Pinky(__Ghost): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int, int],
        size: int,
        speed: int=90,
        maze: Maze,
    ) -> None:
        self._path = "src/assests/frames/pinky.png"
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

    @override
    def position(self) -> tuple[int | float, int | float]:
        return self._ghost.position.x, self._ghost.position.y
