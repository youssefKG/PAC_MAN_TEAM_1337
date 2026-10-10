from typing import override, cast
from src.core.scene import Scene
from src.core import (
    PixelImage,
    Engine,
    ImageType,
    RgbColors,
    GridImage,
)

class GameScene(Scene):

    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension

        self.__background = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=self.__window_width,
                height=self.__window_height,
                position=(0, 0)
            ).set_parent().create()
        )

        self.__background.set_background_color(RgbColors.OLIVE)
        self.__layout_image: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width=.55,
                height=.65,
                image_type=ImageType.GRID_IMAGE,
                row=2,
                col=2,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/darwin_borders.png",
                position=(.5, .5),
            )
            .set_parent(self.__background)
            .to_center().create()
        )
        self.__box_image2: PixelImage = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=.84,
                height=.84,
                time_per_frame=10,
                position=(.5, .5),
            )
            .set_parent(self.__layout_image)
            .to_center().create()
        )
        self.__box_image2.set_background_color(RgbColors.BLACK)

    @override
    def update(self, elapsed_time: float) -> None:
        pass

    def renderer(self) -> None:
        self.__background.to_window()
        self.__layout_image.to_window()
        self.__box_image2.to_window()
