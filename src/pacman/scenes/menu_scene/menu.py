from enum import Enum, auto 
from typing import  cast, Literal
from src.core import (
    ImageType,
    GridImage,
    PixelImage,
    RgbColors,
    Engine,
)
from src.core import Key, EventContainer

BUTTON_LAYOUT_PATH = "src/assests/menu/green_menu.png" 
BUTTON_LAYOUT_COL = 3
BUTTON_LAYOUT_ROW = 3
BUTTON_LAYOUT_TOTAL_COLS = 5
BUTTON_LAYOUT_TOTAL_ROWS = 4
BUTTON_WIDTH = .75
BUTTON_HEIGHT = .23


class MenuButtonType(Enum):
    SETTINGS = auto()
    PLAY = auto()
    HIGH_SCORES = auto()
    QUIT = auto()



class MenuButton:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        position: tuple[int | float, int | float],
        parent: PixelImage,
        text: str,
        type:MenuButtonType,
        is_visible: bool = False
     ) -> None:
        self.__engine: Engine = engine
        self.__type: MenuButtonType = type
        self.__is_visible: bool = is_visible
        self.__button_container: GridImage = cast(
            GridImage, 
                self.__engine.new_image(
                    width=BUTTON_WIDTH,
                    height=BUTTON_HEIGHT,
                    image_type=ImageType.GRID_IMAGE,
                    row=BUTTON_LAYOUT_ROW,
                    col=BUTTON_LAYOUT_COL,
                    total_cols=BUTTON_LAYOUT_TOTAL_COLS,
                    total_rows=BUTTON_LAYOUT_TOTAL_ROWS,
                    path=BUTTON_LAYOUT_PATH,
                    position=position,
                )
                .set_parent(parent)
                .center_x()
                .create()
        )
        self.__button_background: PixelImage = cast(
                PixelImage,
                self.__engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.78,
                    height=.85,
                    time_per_frame=10,
                    position=(.5, .5),
                    is_visible=self.__is_visible
                )
                .set_parent(self.__button_container)
                .to_center().create()
        )
        self.__button_background.set_background_color(RgbColors.GREEN)
        self.__button_background.add_text(
            self.__engine.new_text(
                text=text,
                lettere_spacing=3,
                font_size=28,
                color=RgbColors.WHITE).to_center(),
                position=(.5, .5)
        )

    def toggle_background(self) -> None:
        self.__button_background.toggle()

    @property
    def type(self) -> MenuButtonType:
        return self.__type

class Menu:
    def __init__(
        self,
        *,
        parent: PixelImage,
        engine: Engine,
        event_container: EventContainer,
    ) -> None:
        self._engine: Engine = engine
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
        self.__menu_buttons: list[MenuButton] = [
            MenuButton(
                engine=self._engine,
                parent=self.__menu_background,
                position=(.5, .01),
                text="PLAY",
                is_visible=True,
                type=MenuButtonType.SETTINGS
            ),
            MenuButton(
                engine=self._engine,
                parent=self.__menu_background,
                position=(.5, .25),
                text="settings",
                type=MenuButtonType.PLAY
            ),
            MenuButton(
                engine=self._engine,
                parent=self.__menu_background,
                position=(.5, .50),
                text="HIGH SCORES",
                type=MenuButtonType.HIGH_SCORES
            ),
            MenuButton(
                engine=self._engine,
                parent=self.__menu_background,
                position=(.5, .75),
                text="QUIT",
                type=MenuButtonType.QUIT
            )
        ]
        self.__current_active_button_idx = 0;

    @property
    def active_button(self) -> MenuButtonType:
        return self.__menu_buttons[self.__current_active_button_idx].type

    def on_change(self, pressed_key: Literal[Key.UP, Key.DOWN]) -> None:
        match pressed_key:
            case Key.DOWN:
                self.__menu_buttons[self.__current_active_button_idx].toggle_background()
                if self.__current_active_button_idx == len(self.__menu_buttons) - 1:
                    self.__current_active_button_idx = 0;
                else:
                    self.__current_active_button_idx += 1
                self.__menu_buttons[self.__current_active_button_idx].toggle_background()
            case Key.UP:
                self.__menu_buttons[self.__current_active_button_idx].toggle_background()
                if self.__current_active_button_idx == 0:
                    self.__current_active_button_idx = len(self.__menu_buttons) -1;
                else:
                    self.__current_active_button_idx -= 1
                self.__menu_buttons[self.__current_active_button_idx].toggle_background()
