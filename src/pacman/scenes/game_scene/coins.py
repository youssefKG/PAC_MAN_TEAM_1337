
from src.pacman.scenes.common import Entity
from src.core import Engine, PixelImage, PngImage, FrameImage, ImageType


class Coin(Entity):

    def __init__(
        self,
        /, *,
        engine: Engine,
        parent: PixelImage | PngImage,
        position: tuple[int, int],
        size: int,
    ) -> None:
        self._path: str = "src/assests/frames/coin.png"
        super().__init__(
            engine=engine,
            parent=parent,
            size=size,
            position=position
        )
        self._coin: FrameImage = self.__new_coin()


    def __new_coin(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=self._size * 2,
            height=self._size * 2,
            path=self._path,
            time_per_frame=.1,
            position=self._position,
            frames=8
        ).set_parent(self._parent).create()

    def update(self, elapsed_time: float) -> None:
        self._coin.update(elapsed_time)

