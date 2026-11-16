from typing import override

from src.pacman.scenes.base import BaseScene
from src.pacman.game_state import GameStateManager, GameState
from src.core import Engine

class InstructionsScene(BaseScene):
    def __init__(self, engine: Engine, game_state_manager: GameStateManager) -> None:
        super().__init__(engine=engine)
        self.__game_state_manager: GameStateManager = game_state_manager

    @override
    def mount(self) -> None:
        pass

    @override
    def unmount(self) -> None:
        pass

    @override
    def update(self, elapsed_time: float) -> None:
        pass


__all__ = ["InstructionsScene"]
