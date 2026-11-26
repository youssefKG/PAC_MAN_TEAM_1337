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
        self.__engine.game_loop(lambda elapsed_time: self.__scene_manager.update(elapsed_time))

    def stop(self) -> None:
        self.__engine.close_window()

__all__ = ["Pacman"]
