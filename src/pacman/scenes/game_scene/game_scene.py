from typing import override
from src.pacman.scenes.base import BaseScene
from src.core import (
    Engine,
)
from src.pacman.game_state import GameState, GameStateManager

class GameScene(BaseScene):
    def __init__(self, engine: Engine, game_state: GameStateManager) -> None:
        super().__init__(engine)

    @override
    def mount(self) -> None:
        super().mount()

    @override
    def unmount(self) -> None:
        super().unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        ...
