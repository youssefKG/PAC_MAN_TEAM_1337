from typing import cast

from src.core import Engine, FrameImage, ImageType, PixelImage, GridImage

class Guide:
    def __init__(self, *, engine: Engine, parent: PixelImage) -> None:
        self.__engine: Engine = engine
        self.__parent: PixelImage = parent
        self.__guide_wrapper: GridImage = self.__new_instruction_wrapper()
        self.__guide_character: FrameImage = self.__new_guide_character()

    def update(self, elapsed_time: float) -> None:
        self.__guide_character.update(elapsed_time)

    def __new_instruction_wrapper(self) -> GridImage:
        return cast(
            GridImage, 
            self.__engine.new_image(
                image_type=ImageType.GRID_IMAGE,
                width=.3,
                height=.4,
                total_cols=5,
                total_rows=4,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=(.1, .5)
            )
            .set_parent(self.__parent)
            .center_y()
            .create()
        )

    def __new_guide_character(self) -> FrameImage:
        return cast(
            FrameImage,
            self.__engine.new_image(
                image_type=ImageType.FRAME_IMAGE,
                width=.08,
                height=.1,
                time_per_frame=0.2,
                path="src/assests/idle.png",
                position=(.1, .5),
                frames=4
            )
            .set_parent(self.__guide_wrapper)
            .to_center()
            .create()
       )

