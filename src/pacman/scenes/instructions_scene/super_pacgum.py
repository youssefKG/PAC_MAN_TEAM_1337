from .entities import Entity
from src.core import Engine, FrameImage, ImageType, PngImage, PixelImage
from .maze import Maze

class SuperPacgum(Entity):
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
        self._pacgum: FrameImage = self.__new_pacgum()
        self._maze: Maze = maze

    def __new_pacgum(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=self._size,
            height=self._size,
            path="src/assests/light_gum.png",
            time_per_frame=.1,
            position=self._position,
            frames=8
        ).set_parent(self._parent).create()

    def update(self, elapsed_time: float) -> None:
        self._pacgum.update(elapsed_time)
