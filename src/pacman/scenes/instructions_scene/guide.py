from typing import cast

from src.core import (
    Engine,
    FrameImage,
    ImageType,
    PixelImage,
    GridImage,
    RgbColors,
    PngImage
)

class Guide:
    def __init__(self, *, engine: Engine, parent: PixelImage) -> None:
        self.__engine: Engine = engine
        self.__parent: PixelImage = parent
        # self.__guide_wrapper: GridImage = self.__new_instruction_wrapper()
        self.__guide_background: PixelImage = self.__new_guide_background()
        self.__guide_character: FrameImage = self.__new_guide_character()
        self.__dialogue: PngImage = self.__new_dialogue()
        self.__add_text_to_dialogue(
            "Hey stranger Welcome to the world of\nPacMan A place full of twists surprises \nand mischievous ghosts Ready for a little\nadventure"
        )

    def update(self, elapsed_time: float) -> None:
        self.__guide_character.update(elapsed_time)

    def __new_instruction_wrapper(self) -> GridImage:
        return cast(
            GridImage, 
            self.__engine.new_image(
                image_type=ImageType.GRID_IMAGE,
                width=.3,
                height=.2,
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
                width=.25,
                height=.8,
                time_per_frame=0.2,
                path="src/assests/idle.png",
                position=(.1, .5),
                frames=4
            )
            .set_parent(self.__guide_background)
            .to_center()
            .create()
       )

    def __new_guide_background(self) -> PixelImage:
        maze_background: PixelImage = cast(
            PixelImage,
            self.__engine.new_image(
                width=.30,
                height=.20,
                image_type=ImageType.PIXEL_IMAGE,
                position=(.1, .5)
            ).set_parent(self.__parent)
            .center_y()
            .create()
          )
        # maze_background.set_background_color(RgbColors.TRANSPARENT_GREEN)
        return maze_background

    def __new_dialogue(self) -> PngImage:
        dialogue_message: PngImage = cast(
            PngImage,
            self.__engine.new_image(
                image_type=ImageType.PNG_IMAGE,
                width=0.7,
                height=0.3,
                path="src/assests/dialogue/dialogue.png",
                position=(.5, .4)
            ).set_parent(self.__guide_background).to_center().create()
        )
        return dialogue_message

    def __add_text_to_dialogue(self, text: str) -> None:
        self.__dialogue.add_text(
            text=self.__engine.new_text(
                font_size=13,
                lettere_spacing=1,
                color=RgbColors.BLACK,
                text=text
            ),
            position=(.04, .12)
        )
