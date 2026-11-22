from typing import override, cast

from src.core import Engine, PixelImage, ImageType, Key
from src.pacman.game_state import GameStateManager, GameState

from src.pacman.scenes.base import BaseScene

from src.mazegenerator import MazeGenerator

from .maze import Maze
from .guide import Guide

VERTICAL_CELLS = 14
HORIZONTAL_CELLS = 14

class InstructionsScene(BaseScene):
    def __init__(
        self,
        engine: Engine,
        game_state_manager: GameStateManager
    ) -> None:
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
        self.__maze_generator: MazeGenerator = MazeGenerator(
            size=(HORIZONTAL_CELLS, VERTICAL_CELLS)
        )
        self.__maze_generator.generate()
        self.__guide: Guide = Guide(
            engine=self._engine,
            parent=self.__scene_container
        )
        self.__maze: Maze = Maze(
            engine=self._engine,
            maze_generator=self.__maze_generator,
            parent=self.__scene_container,
            vertical_cells=VERTICAL_CELLS,
            horizontal_cells=HORIZONTAL_CELLS,
        )
        self.__maze.draw()
        self.__set_events_to_events_container()

    @override
    def mount(self) -> None:
        super().mount()
        self.__scene_container.mount()

    def __move_pacman(self, pressed_key: Key) -> None:
        match pressed_key:
            case Key.LEFT:
                pass
            case _:
                pass

    def __on_key_pressed(self, pressed_key: Key) -> None:
        match pressed_key:
            case Key.ESC:
                self.unmount()
                self.__game_state_manager.change_state(GameState.MENU)
            case _:
                pass

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__scene_container.unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        self.__maze.update(elapsed_time)
        self.__guide.update(elapsed_time)

    def __set_events_to_events_container(self) -> None:
        self._events_container.add_event(key=Key.ESC, callback=lambda: self.__on_key_pressed(Key.ESC))
        self._events_container.add_event(key=Key.LEFT, callback=lambda: self.__move_pacman(Key.LEFT))
        self._events_container.add_event(key=Key.J, callback=lambda: self._engine.close_window())

__all__ = ["InstructionsScene"]
