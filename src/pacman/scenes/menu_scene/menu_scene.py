from typing import cast
from src.core import (
    ImageType,
    PixelImage,
    RgbColors,
    Engine,
)
from .menu import Menu
from src.pacman.scenes.base import BaseScene
from src.core.event import Key


TOTAL_SPIRITS = 90

class MenuScene(BaseScene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
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
        self.__black_transparent_background.add_text(
            self._engine.new_text(
                text="PACMAN 1337",
                font_size=55,
                lettere_spacing=3,
                color=RgbColors.WHITE
            ).center_x(),
            (.5, 0.01))
        self.__menu: Menu = Menu(parent=self.__black_transparent_background , engine=self._engine)


    def update(self, elapsed_time: float) -> None:
        self.__menu.update(elapsed_time)

    def renderer(self) -> None:
        self.__black_transparent_background.mount()
        self.__black_transparent_background.add_event(Key.KEY_J, self.__black_transparent_background.unmount)
        self.__black_transparent_background.add_event(Key.KEY_K, self.__black_transparent_background.mount)


    @property
    def parent(self) -> PixelImage:
        return self.__black_transparent_background
