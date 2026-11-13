import sys
from uuid import uuid4
from typing import override, cast
from src.core import (
    Engine,
    PngImage,
    ImageType,
    PixelImage,
    GridImage,
    RgbColors,
    Key
)
from src.pacman.game_state import GameStateManager, GameState
from src.pacman.scenes.base import BaseScene



class PlayerScore:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        name: str,
        rank: int,
        parent: PixelImage,
        position: tuple[float | int, float | int],
        is_visible: bool = False
    ) -> None:
        self.__id: str = str(uuid4())
        self.__name: str = name
        self.__rank: int = rank
        self.__parent: PixelImage = parent
        self.__engine: Engine = engine
        self.__position: tuple[float | int, float | int] = position
        self.__is_visible: bool = is_visible
        self.__background_image: PixelImage  = cast(
            PixelImage,
            self.__engine.new_image(
                width=1.,
                height=0.2,
                image_type=ImageType.PIXEL_IMAGE,
                is_visible=self.__is_visible,
                position=self.__position,
            ).set_parent(self.__parent).to_center().create()
        )
        self.__background_image.set_background_color(RgbColors.BROWN)
        self.__badge: GridImage = cast(
            GridImage,
            self.__engine.new_image(
                width=0.2,
                height=1.,
                image_type=ImageType.PNG_IMAGE,
                path="src/assests/badges/badges.png",
                position=(0.1, 0.)
            )
            .set_parent(self.__background_image)
            .create()
        )
    def id(self) -> str:
        return self.__id

    def toggle_background(self) -> None:
        self.__background_image.toggle()

    def get_rank_badge(self) -> GridImage:
        match self.__rank:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                ...
        return cast(
            GridImage,
            self.__engine.new_image(
                width=0.2,
                height=1.,
                image_type=ImageType.GRID_IMAGE,
                col=9,
                row=7,
                total_cols=10,
                total_rows=10,
                path="src/assets/badges/badges.png"
            ).set_parent(self.__background_image).create()
        )


class HighScoresScene(BaseScene):
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        game_state_manager: GameStateManager
    ) -> None:
        super().__init__(engine)
        self.__engine: Engine = engine
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__window_width, self.__window_height = self.__engine.window_dimension
        self.__container: PixelImage = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=self.__window_width,
                height=self.__window_height,
                position=(0, 0)
            )
            .set_parent()
            .create()
        )
        self.__container.set_background_color(RgbColors.GREEN)
        self.__banner: GridImage = cast(
            GridImage, 
            self._engine.new_image(
                width=.65,
                height=0.75,
                image_type=ImageType.GRID_IMAGE,
                total_rows=4,
                total_cols=5,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=(0.5, .12)
            )
            .set_parent(self.__container)
            .center_x()
            .create()
        )
        self.__banner_background: PixelImage = cast(
            PixelImage,
            self.__engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=.80,
                height=.75,
                position=(.5, .5),
            )
            .set_parent(self.__banner)
            .to_center()
            .create()
        )
        self.__banner_background.set_background_color(RgbColors.ORANGE)
        self.__player_score: PlayerScore = PlayerScore(
            engine=self.__engine,
            parent=self.__banner_background,
            position=(.5, .0),
            is_visible=True,
            name="YOUSSEF",
            rank=0
        )

    @override
    def mount(self) -> None:
        super().mount()
        self.__container.mount()
        self._events_container.add_event(key=Key.J, callback=self.change)

    def change(self) -> None:
        self.unmount()
        self.__game_state_manager.change_state(GameState.MENU)

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__container.unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        pass
