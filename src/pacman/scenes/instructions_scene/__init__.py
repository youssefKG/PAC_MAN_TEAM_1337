from typing import override, cast

from src.pacman.scenes.base import BaseScene
from src.pacman.game_state import GameStateManager, GameState
from src.pacman.scenes.common import Maze
from src.core import Engine, PixelImage, ImageType

class InstructionsScene(BaseScene):
    def __init__(self, engine: Engine, game_state_manager: GameStateManager) -> None:
        super().__init__(engine=engine)
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__scene_container: PixelImage = cast(
            PixelImage,
            self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=self.__window_width,
                height=self.__window_height,
                position=(0, 0),
            ).set_parent().create()
        )
        self.__maze: Maze = Maze(
            engine=self._engine,
            parent=self.__scene_container,
            width=.4,
            height=.5,
            vertical_cells=10,
            horizontal_cells=10,
            position=(.6, .2)
        )

    @override
    def mount(self) -> None:
        self.__scene_container.mount()

    @override
    def unmount(self) -> None:
        pass

    @override
    def update(self, elapsed_time: float) -> None:
        pass


__all__ = ["InstructionsScene"]
