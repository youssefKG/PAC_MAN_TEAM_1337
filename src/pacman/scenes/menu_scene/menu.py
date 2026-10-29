from enum import Enum, auto
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
from src.core import Key, EventContainer
from src.pacman.game_state import PacmanState, GameState

BUTTON_LAYOUT_PATH ="src/assests/menu/green_menu.png" 
BUTTON_LAYOUT_COL = 3
BUTTON_LAYOUT_ROW = 3
BUTTON_LAYOUT_TOTAL_COLS = 5
BUTTON_LAYOUT_TOTAL_ROWS = 4
BUTTON_WIDTH = .85
BUTTON_HEIGHT = .3
GHOST_WIDTH = .05
GHOST_HEIGHT = .08

class MenuButton(Enum):
    SETTINGS = auto()
    PLAY = auto()
    QUIT = auto()

class Menu:
    def __init__(
            self,
            *,
            parent: PixelImage,
            engine: Engine,
            event_container: EventContainer,
            pacman_state: PacmanState
            ) -> None:
        self._engine: Engine = engine
        self.__pacman_state: PacmanState = pacman_state
        self.__active_button: MenuButton = MenuButton.SETTINGS
        self.__event_container: EventContainer = event_container
        self.__parent: PixelImage = parent
        self.__menu_wrapper: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width= .25,
                height=.40,
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
        self.__menu_background: PixelImage = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=.7,
                height=.7,
                position=(.5, .5),
            )
            .set_parent(self.__menu_wrapper)
            .to_center().create()
        )
        self.__menu_background.set_background_color(RgbColors.GREEN)
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
                    ).set_parent(self.__menu_background).to_center().create()
        )
        self.__settings_button_background: PixelImage = cast(
                PixelImage,
                self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.78,
                    height=.85,
                    time_per_frame=10,
                    position=(.5, .5),
                    )
                .set_parent(self.__settings_button)
                .to_center().create()
                )
        self.__settings_button_background.set_background_color(RgbColors.GREEN)
        self.__settings_button.add_text(
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
                    position=(.5, .5)
                    ).set_parent(self.__menu_background).to_center().create()
                )
        self.__play_button_background : PixelImage = cast(
                PixelImage,
                self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.78,
                    height=.85,
                    time_per_frame=10,
                    position=(.5, .5),
                    )
                .set_parent(self.__play_button)
                .to_center().create()
                )
        self.__play_button_background.set_background_color(RgbColors.GREEN)
        self.__play_button_background.hide()
        self.__play_button.add_text(
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
                    position=(.5, .80)
                    ).set_parent(self.__menu_background).to_center().create()
                )
        self.__quit_button_background: PixelImage = cast(
                PixelImage,
                self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.78,
                    height=.85,
                    time_per_frame=10,
                    position=(.5, .5),
                    )
                .set_parent(self.__quit_button)
                .to_center().create()
                )
        self.__quit_button_background.set_background_color(RgbColors.GREEN)
        self.__quit_button_background.hide()
        self.__quit_button.add_text(
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
                    ).set_parent(self.__menu_background).create()
                )
        self.__orange_ghost_target_vector = Vector2(
                x=self.__menu_background.position.x,
                y=self.__menu_background.position.y
                )
        self.__event_container.add_event(
            key=Key.KEY_J,
            callback=lambda: self.on_active_button_change(Key.KEY_J)
        )
        self.__event_container.add_event(
            key=Key.KEY_ENTER,
            callback=lambda: self.on_active_button_change(Key.KEY_ENTER)
        )

    def update(self, elapsed_time: float) -> None:
        # ***************** ORANGE_GHOST ************************
        end: float = self.__menu_background.position.x + self.__menu_background.width - self.__orange_ghost.width
        if (self.__orange_ghost.position.x >= end):
            self.__orange_ghost_target_vector.x = self.__menu_background.position.x
        elif (
                self.__orange_ghost.position.x <= self.__menu_background.position.x
                ):
            self.__orange_ghost_target_vector.x = self.__menu_background.position.x - GHOST_WIDTH + self.__menu_background.width
        self.__orange_ghost.move_to(
                target=self.__orange_ghost_target_vector,
                dt=elapsed_time,
                speed_per_frame_unit=45,
                )
        self.__orange_ghost.update(elapsed_time)

    def on_active_button_change(self, key: Key) -> None:
        match key:
            case Key.KEY_J:
                match self.__active_button:
                    case MenuButton.SETTINGS:
                        self.__active_button = MenuButton.PLAY
                        self.__settings_button_background.hide()
                        self.__play_button_background.display()
                    case MenuButton.PLAY:
                        self.__active_button = MenuButton.QUIT
                        self.__play_button_background.hide()
                        self.__quit_button_background.display()
                    case MenuButton.QUIT:
                        self.__active_button = MenuButton.SETTINGS
                        self.__quit_button_background.hide()
                        self.__settings_button_background.display()
            case Key.KEY_K:
                match self.__active_button:
                    case MenuButton.SETTINGS:
                        self.__active_button = MenuButton.QUIT
                        self.__settings_button_background.unmount()
                        self.__quit_button_background.mount()
                    case MenuButton.PLAY:
                        self.__active_button = MenuButton.SETTINGS
                        self.__play_button_background.unmount()
                        self.__settings_button_background.mount()
                    case MenuButton.QUIT:
                        self.__active_button = MenuButton.PLAY
                        self.__quit_button_background.unmount()
                        self.__play_button_background.mount()
            case Key.KEY_ENTER:
                match self.__active_button:
                    case MenuButton.SETTINGS:
                        self.__pacman_state.change(GameState.SETTINGS)
                        self.__menu_wrapper.unmount()
                    case MenuButton.PLAY:
                        self.__pacman_state.change(GameState.PLAY)
                        self.__menu_wrapper.unmount()
                    case MenuButton.QUIT:
                        self.__pacman_state.change(GameState.QUIT)
                        self.__menu_wrapper.unmount()
            case _:
                pass
