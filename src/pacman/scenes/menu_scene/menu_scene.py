from typing import cast
from src.core import (
    ImageType,
    PixelImage,
    RgbColors,
    Engine,
    FrameImage,
    GridImage
)
from .menu import Menu
from src.pacman.scenes.base import BaseScene
from src.core.event import Key
from src.pacman.game_state import PacmanState


TOTAL_SPIRITS = 90

class MenuScene(BaseScene):
    def __init__(self, engine: Engine, pacman_state: PacmanState) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
        self.__pacman_state: PacmanState = pacman_state
        self.__black_transparent_background = cast(
                PixelImage,
                    self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    position=(0, 0),
              ).set_parent().create()
        )
        self.__black_transparent_background.set_background_color(RgbColors.BLACK_TRANS)
        self.__banner: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width= 0.3,
                    height=0.1,
                    image_type=ImageType.GRID_IMAGE,
                    row=5,
                    col=4,
                    total_cols=5,
                    total_rows=8,
                    path="src/assests/15.png",
                    position=(.50, .0)
            ).set_parent(self.__black_transparent_background).center_x().create()
        )
        self.__banner.add_text(
            self._engine.new_text(
                text="PACMAN 42 PARIS",
                font_size=40,
                lettere_spacing=7,
                color=RgbColors.WHITE
            ).to_center(),
            (.5, 0.5)
        )
        self.__menu: Menu = Menu(
            parent=self.__black_transparent_background ,
            engine=self._engine,
            event_container=self._events_container,
            pacman_state=self.__pacman_state
        )

    def update(self, elapsed_time: float) -> None:
        self.__menu.update(elapsed_time)

    def quit(self) -> None:
        pass

    def renderer(self) -> None:
        self._events_container.on()
        self.__black_transparent_background.mount()

    @property
    def parent(self) -> PixelImage:
        return self.__black_transparent_background
