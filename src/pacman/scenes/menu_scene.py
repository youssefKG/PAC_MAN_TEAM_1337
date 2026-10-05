from typing import override, cast
from src.core import FrameImage, ImageType
from src.core import Scene, Engine

class MenuScene(Scene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
        self.__top_spinner: FrameImage = cast(
            FrameImage,
            cast(
                object,
                self._engine.new_image(
                    image_type=ImageType.FRAME_IMAGE,
                    width=100,
                    height=100,
                    frames=7,
                    time_per_frame=2,
                )
           )
      )

    @override
    def update(self, elapsed_time: float) -> None:
        self.__top_spinner.update(elapsed_time)
