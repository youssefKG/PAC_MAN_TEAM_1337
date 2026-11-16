from typing import cast
from src.core import PixelImage, Engine, RgbColors, ImageType

class PlayersLeaderboardTableHeader:
    def __init__(self, *, engine: Engine, parent: PixelImage) -> None:
        self.__engine: Engine = engine
        self.__parent: PixelImage = parent
        self.__players_score_table_header_background: PixelImage = cast(
            PixelImage,
            self.__engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=1.,
                height=0.09,
                position = (.5, .0),
            )
            .set_parent(self.__parent)
            .center_x()
            .create()
        )
        self.__players_score_table_header_background.set_background_color(RgbColors.GREEN)
        self.__players_score_table_header_background.add_text(
            text=self.__engine.new_text(
                text="RANK",
                color=RgbColors.WHITE,
                font_size=20,
                lettere_spacing=3
            )
            .center_y(),
            position=(.02, 0.5)
        )
        self.__players_score_table_header_background.add_text(
            text=self.__engine.new_text(
                text="NAMES",
                color=RgbColors.WHITE,
                font_size=20,
                lettere_spacing=3
            )
            .center_y(),
            position=(.2, 0.5)
        )
        self.__players_score_table_header_background.add_text(
            text=self.__engine.new_text(
                text="POINTS",
                color=RgbColors.WHITE,
                font_size=20,
                lettere_spacing=3
            )
            .center_y(),
            position=(.8, 0.5)
        )
