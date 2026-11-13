from typing import override
from src.core import Engine
from src.pacman.scenes.base import BaseScene
from src.pacman.game_state import GameStateManager

class SettingsScene(BaseScene):
    def __init__(self, engine: Engine,  game_state_manager: GameStateManager) -> None:
        super().__init__(engine)
        self.__game_state_manager: GameStateManager = game_state_manager

    @override
    def mount(self) -> None:
        super().mount()

    @override
    def unmount(self) -> None:
        super().unmount()
