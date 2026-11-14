from typing import  cast
from src.core import (
    Engine,
    ImageType,
    PixelImage,
    GridImage,
    RgbColors,
    PngImage,
)
from .player_score import PlayerScore
from src.pacman.game_state import GameStateManager


class LeaderBoard:
    def __init__(
        self,
        engine: Engine,
        parent: PixelImage,
        game_state_manager: GameStateManager
    ) -> None:
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__engine: Engine = engine
        self.__parent: PixelImage = parent
        self.__leaderboard: GridImage = cast(
            GridImage, 
            self.__engine.new_image(
                width=.35,
                height=0.64,
                image_type=ImageType.GRID_IMAGE,
                total_rows=4,
                total_cols=5,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=(0.5, .2)
            )
            .set_parent(self.__parent)
            .center_x()
            .create()
        )
        self.__leaderboard_panel: GridImage = cast(
            GridImage,
            self.__engine.new_image(
                width=.8,
                height=.1,
                image_type=ImageType.GRID_IMAGE,
                total_rows=4,
                total_cols=5,
                col=0,
                row=1,
                path="src/assests/menu/green_menu.png",
                position=(0.5, -.084),
            )
            .set_parent(self.__leaderboard).center_x().create()
        )
        self.__leaderboard_panel.add_text(
            text=self.__engine.new_text(
                    text="LEADERBOARD",
                    font_size=24,
                    lettere_spacing=4,
                    color=RgbColors.WHITE,
              ).to_center(),
            position=(0.5, 0.5)
        )
        self.__wood_background: PngImage = cast(
            PngImage,
            self.__engine.new_image(
                image_type=ImageType.PNG_IMAGE,
                width=.762,
                height=.74,
                position=(.492, .494),
                path="src/assests/backgrounds/wood_background.png"
            )
            .set_parent(self.__leaderboard)
            .to_center()
            .create()
        )
        self.__black_transparent_background: PixelImage = cast(
           PixelImage,
           self.__engine.new_image(
               width=1.,
               height=1.,
               image_type=ImageType.PIXEL_IMAGE,
               position=(.0, .0)
           )
          .set_parent(self.__wood_background)
          .create()
        )
        self.__black_transparent_background.set_background_color(RgbColors.BLACK_TRANS)
