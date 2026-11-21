from src.pacman.game_state import GameStateManager, GameState
from src.core import (
    Engine,
    engine,
)
from src.pacman.scenes import SceneManager

class Pacman:
    def __init__(self) -> None:
        self.__engine: Engine = engine(
           title="PACMAN",
           monitor_size=True,
        )
        self.__game_state_manager: GameStateManager = GameStateManager(
            default_state=GameState.INSTRUCTIONS
        )
        self.__scene_manager: SceneManager = SceneManager(
            engine=self.__engine,
            game_state_manager=self.__game_state_manager
        )

    def run(self) -> None:
        self.__engine.game_loop(self.__update)

    def __update(self, elapsed_time: float) -> None:
        self.__scene_manager.update(elapsed_time)

__all__ = ["Pacman"]
