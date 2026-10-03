from typing import cast
from src.core import (
    Engine,
    ImageInterface,
    RgbColors,
    Vector2,
    FrameImage, 
    ImageFormat,
)
from enum import Enum

IMAGE_WIDTH = 100
IMAGE_HEIGHT = 100


class GameState(Enum):
    pass


class Pacman:
    def __init__(
        self,
     ) -> None:
        self.__engine: Engine = Engine(200, 200, title="Pacman")
        self.__engine.set_window_to_monitor_size()
        self.__box_image: ImageInterface = self.__engine.new_image(
            width=IMAGE_WIDTH,
            height=IMAGE_HEIGHT,
            image_format=ImageFormat.PIXEL
        )
        self.__box_image.to_window()
        self.__box_image.set_background_color(RgbColors.PINK)
        # self.__orange_ghost_image: FrameImage = cast(FrameImage, self.__engine.new_image(
        #     width=IMAGE_WIDTH,
        #     height=IMAGE_HEIGHT ,
        #     frames=7,
        #     image_format=ImageFormat.PNG,
        #     path="orange_ghost.png"
        # ))
        # self.__orange_ghost_image.to_window()


    def run(self) -> None:
        self.__engine.game_loop(self.__update)


    def __update(self, elapsed_time: float) -> None:
        self.__box_image.move(Vector2(x=elapsed_time + 1, y=elapsed_time + 1))
        self.__box_image.update()

__all__ = ["Pacman"]
