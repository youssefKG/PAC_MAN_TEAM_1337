from typing import  cast
from src.core import (
    FrameImage,
    ImageType,
    GridImage,
    PixelImage,
    RgbColors,
    Engine,
    Vector2,
)
from src.pacman.utils import PacmanAssetsPath

BUTTON_LAYOUT_PATH ="src/assests/menu/green_menu.png" 
BUTTON_LAYOUT_COL = 3
BUTTON_LAYOUT_ROW = 2
BUTTON_LAYOUT_TOTAL_COLS = 5
BUTTON_LAYOUT_TOTAL_ROWS = 4
BUTTON_WIDTH = .5
BUTTON_HEIGHT = .2
GHOST_WIDTH = .03
GHOST_HEIGHT = .05

class Menu:
    def __init__(self, *, parent: PixelImage, engine: Engine) -> None:
        self._engine: Engine = engine
        self.__layout_image: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width= .45,
                height=.60,
                image_type=ImageType.GRID_IMAGE,
                row=3,
                col=4,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/green_menu.png",
                position=(.5, .5),
            )
            .set_parent(parent)
            .to_center().create()
        )
        self.__box_image2: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__layout_image)
                .to_center().create()
        )
        self.__box_image2.set_background_color(RgbColors.GREEN)
        # ********************* START SETTINGS **********************
        self.__settings_button: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    image_type=ImageType.GRID_IMAGE,
                    row=BUTTON_LAYOUT_ROW,
                    col=BUTTON_LAYOUT_COL,
                    total_cols=BUTTON_LAYOUT_TOTAL_COLS,
                    total_rows=BUTTON_LAYOUT_TOTAL_ROWS,
                    path=BUTTON_LAYOUT_PATH,
                    position=(.5, .2)
                ).set_parent(self.__box_image2).to_center().create()
        )
        self.__setting_button_background: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__settings_button)
                .to_center().create()
        )
        self.__setting_button_background.add_text(
                self._engine.new_text(
                    text="SETTINGS",
                    lettere_spacing=3,
                    font_size=28,
                    color=RgbColors.WHITE).to_center(),
                    position=(.5, .5)
        )
        # ********************* END SETTINGS **********************
        # ********************* START PLAY BUTTON **********************
        self.__play_button: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    image_type=ImageType.GRID_IMAGE,
                    row=BUTTON_LAYOUT_ROW,
                    col=BUTTON_LAYOUT_COL,
                    total_cols=BUTTON_LAYOUT_TOTAL_COLS,
                    total_rows=BUTTON_LAYOUT_TOTAL_ROWS,
                    path=BUTTON_LAYOUT_PATH,
                    position=(.5, .42)
                ).set_parent(self.__box_image2).to_center().create()
        )
        self.__play_button_background : PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__play_button)
                .to_center().create()
        )
        # self.__box_image3.set_background_color(RgbColors.BLACK)
        self.__play_button_background.add_text(
                self._engine.new_text(
                  text="PLAY",
                  lettere_spacing=3,
                  font_size=28,
                  color=RgbColors.WHITE
              )
              .to_center(), position=(.5, .5))
        # ********************* END PALAYR **********************

        # ********************* START QUIT *************************
        self.__quit_button: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    image_type=ImageType.GRID_IMAGE,
                    row=BUTTON_LAYOUT_ROW,
                    col=BUTTON_LAYOUT_COL,
                    total_cols=BUTTON_LAYOUT_TOTAL_COLS,
                    total_rows=BUTTON_LAYOUT_TOTAL_ROWS,
                    path=BUTTON_LAYOUT_PATH,
                    position=(.5, .64)
                ).set_parent(self.__box_image2).to_center().create()
        )
        self.__quit_button_background: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__quit_button)
                .to_center().create()
        )
        # self.__box_image3.set_background_color(RgbColors.BLACK)
        self.__quit_button_background.add_text(
                self._engine.new_text(
                  text="QUIT",
                  lettere_spacing=3,
                  font_size=28,
                  color=RgbColors.WHITE
              )
              .to_center(), position=(.5, .5))
        # ********************* END QUIT *************************

        # ********************* START GHOSTS **********************
        self.__orange_ghost: FrameImage = cast(
            FrameImage,
            self._engine.new_image(
                width=GHOST_WIDTH,
                height=GHOST_HEIGHT,
                frames=8,
                image_type=ImageType.FRAME_IMAGE,
                path=PacmanAssetsPath.ORANGE_GHOST_FRAME,
                time_per_frame=.17,
                position=(0, 0)
            ).set_parent(self.__box_image2).create()
        )
        self.__orange_ghost_target_vector = Vector2(
            x=self.__box_image2.position.x,
            y=self.__box_image2.position.y
        )
        # self.__blue_ghost: FrameImage = cast(
        #         FrameImage,
        #         self._engine.new_image(
        #             width=GHOST_WIDTH,
        #             height=GHOST_HEIGHT,
        #             image_type=ImageType.FRAME_IMAGE,
        #             path=PacmanAssetsPath.BLUE_GHOST_FRAME,
        #             frames=8,
        #             position=(
        #                 self.__box_image2.position.x + self.__box_image2.width - GHOST_WIDTH,
        #                 0
        #             )
        #         ).set_parent(self.__box_image2)
        # )
        # self.__blue_ghost_target_vector = Vector2(
        #     x=float(self.__box_image2.position.x + self.__box_image2.width - GHOST_WIDTH),
        #     y=float(self.__blue_ghost.position.y + self.__box_image2.height - GHOST_HEIGHT)
        # )
        # ********************* END GHOSTS **********************
        

    def update(self, elapsed_time: float) -> None:
        # ***************** ORANGE_GHOST ************************
        if self.__orange_ghost.position.x >= self.__box_image2.position.x + self.__box_image2.width - self.__orange_ghost.width:
            self.__orange_ghost_target_vector.x = self.__box_image2.position.x
        elif self.__orange_ghost.position.x <= self.__box_image2.position.x:
            self.__orange_ghost_target_vector.x = self.__box_image2.position.x - GHOST_WIDTH + self.__box_image2.width
        self.__orange_ghost.move_to(
            target=self.__orange_ghost_target_vector,
            dt=elapsed_time,
            speed_per_frame_unit=45,
        )
        self.__orange_ghost.update(elapsed_time)
        # ***************** END ORANGE_GHOST ************************

        # ***************** END BLUE_GHOST ************************
        # if self.__blue_ghost.position.y >= self.__box_image2.width + GHOST_WIDTH:
        #     self.__blue_ghost_target_vector.y = self.__box_image2.position.y
        # elif self.__blue_ghost.position.y <= self.__box_image2.position.y:
        #     self.__blue_ghost_target_vector.y = self.__box_image2.position.y + self.__box_image2.height - GHOST_HEIGHT
        # self.__blue_ghost.move_to(
        #     target=self.__orange_ghost_target_vector,
        #     dt=elapsed_time,
        #     speed_per_frame_unit=45,
        # )
        # self.__blue_ghost.update(elapsed_time)
        # ***************** END BLUE_GHOST ************************

    def renderer(self) -> None:
        self.__layout_image.to_window()
        self.__box_image2.to_window()
        self.__settings_button.to_window()
        self.__setting_button_background.to_window()
        self.__play_button.to_window()
        self.__play_button_background.to_window()
        self.__quit_button.to_window()
        self.__quit_button_background.to_window()
        self.__orange_ghost.to_window()
        # self.__pacman.to_window()
