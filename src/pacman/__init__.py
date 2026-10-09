from src.pacman.scenes import MenuScene
from src.core import (
    Engine,
    engine,
)

class Pacman:
    def __init__(
        self,
     ) -> None:
        self.__engine: Engine = engine(
           title="PACMAN",
           monitor_size=True,
           # window_width=800,
           # window_height=300
        )
        self.__menu_scene: MenuScene = MenuScene(engine)
        self.__menu_scene.renderer()

    def run(self) -> None:
        self.__engine.game_loop(self.__update)


    def __update(self, elapsed_time: float) -> None:
        self.__menu_scene.update(elapsed_time)

__all__ = ["Pacman"]
