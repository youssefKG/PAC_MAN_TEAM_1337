from typing import override
from src.core import (
    Engine,
    ImageType,
    PixelImage,
    Key
)
from src.pacman.game_state import GameStateManager, GameState
from src.pacman.scenes.base import BaseScene

from .leader_board_table import LeaderBoardTable


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
        self.__scene_container: PixelImage = self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=self.__window_width,
            height=self.__window_height,
            position=(0, 0)
        ).set_parent().create()
        self.__leaderboard: LeaderBoardTable = LeaderBoardTable(
            engine=self._engine,
            parent=self.__scene_container,
            game_state_manager=self.__game_state_manager
        )
    
    @override
    def mount(self) -> None:
        super().mount()
        self.__scene_container.mount()
        self._events_container.add_event(key=Key.ESC, callback=self.change)

    def change(self) -> None:
        self.unmount()
        self.__game_state_manager.change_state(GameState.MENU)

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__scene_container.unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        pass
