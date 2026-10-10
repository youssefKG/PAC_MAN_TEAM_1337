 from typing import override, cast
from src.core.scene import Scene
from src.core import (
    Engine,
    PixelImage,
    GridImage,
    ImageType,
    RgbColors

)


class GameScene(Scene):

    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension

        self.__transparent_background = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=self.__window_width,
                height=self.__window_height,
                position=(0, 0),
            )
        )
        self.__transparent_background.set_background_color(RgbColors.BLACK)
        self.__layout_image: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width=.45,
                height=.45,
                image_type=ImageType.PIXEL_IMAGE,
                row=3,
                col=4,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/nourdine.png",
                position=(.5, .5),
                parent=self.__transparent_background
            )
        )
        self.__layout_image.to_center()
        self.__box_image2: PixelImage = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=.7,
                height=.7,
                time_per_frame=10,
                position=(.5, .5),
                parent=self.__layout_image
            )
        )

        self.__box_image2.set_background_color(RgbColors.OLIVE)
        self.__box_image2.to_center()

    @override
    def update(self, elapsed_time: float) -> None:
           
        pass

    def renderer(self) -> None:
        pass

   def renderer(self) -> None:
        pass

