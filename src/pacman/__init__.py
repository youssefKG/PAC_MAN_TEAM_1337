from typing import cast
from src.core import (
    Engine,
    ImageInterface,
    engine,
    PixelImage,
    RgbColors,
    Vector2,
    FrameImage, 
    ImageFormat,
)

IMAGE_WIDTH = 80
IMAGE_HEIGHT = 80

class Pacman:
    def __init__(
        self,
     ) -> None:
        self.__engine: Engine = engine(monitor_size=True, title="PACMAN")
        # self.__engine.set_window_to_monitor_size()
        self.__box_image: PixelImage = cast(
            PixelImage, self.__engine.new_image(
                width=IMAGE_WIDTH,
                height=IMAGE_HEIGHT,
                image_format=ImageFormat.PIXEL
            )
        )
        self.__box_image.to_window()
        self.__box_image.set_background_color(RgbColors.PINK)
        self.__orange_ghost_image: FrameImage = cast(
            FrameImage,
            cast(
                object, self.__engine.new_image(
                    width=IMAGE_WIDTH,
                    height=IMAGE_HEIGHT ,
                    frames=7,
                    image_format=ImageFormat.PNG,
                    path="orange_ghost.png",
                    time_per_frame=2
                )
             )
        )
        self.__orange_ghost_image.to_window()


    def run(self) -> None:
        self.__engine.game_loop(self.__update)


    def __update(self, elapsed_time: float) -> None:
        self.__orange_ghost_image.move_to(
            target=Vector2(x=1000.0, y=30.0),
            dt=elapsed_time,
            speed_per_frame_unit=3
        )
        self.__box_image.move_to(
            target=Vector2(x=1000, y=1000),
            dt=elapsed_time,
            speed_per_frame_unit=13
        )
        self.__orange_ghost_image.update(elapsed_time)
        self.__box_image.update(elapsed_time)

__all__ = ["Pacman"]
