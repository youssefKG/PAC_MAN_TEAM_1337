from typing import override 
from enum import Enum, auto

from src.core import Engine, PixelImage, ImageType, Key
from src.pacman.game_state import GameStateManager, GameState

from src.pacman.scenes.base import BaseScene
from .entities import Direction
from .pacman import Pacman
from .ghosts import Pinky, Blinky, Clyde
from .super_pacgum import SuperPacgum

from src.mazegenerator import MazeGenerator

from .maze import Maze
from .guide import Guide

VERTICAL_CELLS = 14
HORIZONTAL_CELLS = 14

class TutorialStep(Enum):
    MOVEMENT = auto()
    COLLECT_PAC_DOTS = auto()
    GHOST_INTERACTION = auto()
    GHOST_ACTIVATION = auto()
    DEFEAT = auto()
    VICTORY = auto()

class InstructionsScene(BaseScene):
    def __init__(
        self,
        engine: Engine,
        game_state_manager: GameStateManager
    ) -> None:
        super().__init__(engine=engine)
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__scene_container: PixelImage = self.__new_scene_container()
        self.__maze_generator: MazeGenerator = MazeGenerator(size=(HORIZONTAL_CELLS, VERTICAL_CELLS))
        self.__maze_generator.generate()
        self.__maze_guide_wrapper: PixelImage = self.__new_maze_guide_wrapper()
        self.__guide: Guide = Guide(engine=self._engine, parent=self.__maze_guide_wrapper)
        self.__maze: Maze = self.__new_maze()
        self.__maze.draw()
        self.__pacman: Pacman = self.__new_pacman()
        self.__pinky: Pinky = self.__new_pinky()
        self.__blinky: Blinky = self.__new_blinky()
        self.__clyde: Clyde = self.__new_clyde()
        self.__pacgum: SuperPacgum = self.__new_super_pacgum()
        self.__tutorial_step: TutorialStep = TutorialStep.MOVEMENT
        self.__pressed_keys: list[tuple[Key, Key]] = list()
        self.__add_pacman_events()
        self._events_container.add_event(key=Key.ESC, callback=self.__on_esc_pressed)

    @override
    def mount(self) -> None:
        super().mount()
        self.__scene_container.mount()

    def __on_esc_pressed(self) -> None:
        self.unmount()
        self.__game_state_manager.change_state(GameState.MENU)

    def __new_super_pacgum(self) -> SuperPacgum:
        return  SuperPacgum(
            engine=self._engine,
            parent=self.__maze.maze,
            position=self.__get_position(13, 13),
            size=int(self.__maze.cell_content_size),
            maze=self.__maze
        )

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__scene_container.unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        self.__guide.update(elapsed_time)
        self.__pacman.update(elapsed_time)
        self.__pinky.update(elapsed_time)
        self.__blinky.update(elapsed_time)
        self.__clyde.update(elapsed_time)
        self.__pacgum.update(elapsed_time)

    def on_escape(self) -> None:
        self.unmount()
        self.__game_state_manager.change_state(GameState.MENU)

    def __add_pacman_events(self) -> None:
        # ****************** UP MOVEMENT ***************************
        self._events_container.add_event(key=Key.W, callback=lambda: self.__change_pacman_direction(Key.UP))
        self._events_container.add_event(key=Key.A, callback=lambda: self.__change_pacman_direction(Key.W))

        # ************ DOWN MOVEMENT ***********************
        self._events_container.add_event(key=Key.S, callback=lambda: self.__change_pacman_direction(Key.S))
        self._events_container.add_event(key=Key.D, callback=lambda: self.__change_pacman_direction(Key.DOWN))

        # ************ LEFT MOVEMENT ***********************
        self._events_container.add_event(key=Key.S, callback=lambda: self.__change_pacman_direction(Key.LEFT))
        self._events_container.add_event(key=Key.D, callback=lambda: self.__change_pacman_direction(Key.A))

        # ************ RIGHT MOVEMENT ***********************
        self._events_container.add_event(key=Key.D, callback=lambda: self.__change_pacman_direction(Key.RIGHT))
        self._events_container.add_event(key=Key.S, callback=lambda: self.__change_pacman_direction(Key.D))

    def __change_pacman_direction(self, pressed_key: Key) -> None:
        match pressed_key:
            case Key.UP | Key.W :
                self.__pacman.change_direction(Direction.UP)
                if (Key.UP, Key.W) not in self.__pressed_keys:
                    self.__pressed_keys.append((Key.UP, Key.W))
            case Key.DOWN | Key.S:
                self.__pacman.change_direction(Direction.DOWN)
                if (Key.DOWN, Key.S) not in self.__pressed_keys:
                    self.__pressed_keys.append((Key.DOWN, Key.S))
            case Key.LEFT | Key.A:
                self.__pacman.change_direction(Direction.LEFT)
                if (Key.LEFT, Key.A) not in self.__pressed_keys:
                    self.__pressed_keys.append((Key.LEFT, Key.A))
            case Key.RIGHT | Key.D:
                self.__pacman.change_direction(Direction.RIGHT)
                if (Key.RIGHT, Key.D) not in self.__pressed_keys:
                    self.__pressed_keys.append((Key.RIGHT, Key.D))
            case _:
                ...
        if len(self.__pressed_keys) == 4 and self.__tutorial_step == TutorialStep.MOVEMENT:
            self.__tutorial_step = TutorialStep.COLLECT_PAC_DOTS

    def __new_maze_guide_wrapper(self) -> PixelImage:
        return self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=.8,
            height=0.7,
            position=(.5, .5)
        ).set_parent(self.__scene_container).to_center().create()
        

    def __new_scene_container(self) -> PixelImage:
        return self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=self.__window_width,
            height=self.__window_height,
            position=(0, 0),
        ).set_parent().create()

    def __new_pacman(self) -> Pacman:
        return Pacman(
            engine=self._engine,
            parent=self.__maze.maze,
            position=self.__get_position(0, 0),
            size=int(self.__maze.cell_content_size),
            maze=self.__maze
        )
    
    def __new_pinky(self) -> Pinky:
        return Pinky(
            engine=self._engine,
            parent=self.__maze.maze,
            position=self.__get_position(10, 10),
            size=self.__maze.cell_content_size,
            maze=self.__maze
        )

    def __new_blinky(self) -> Blinky:
        return Blinky(
            engine=self._engine,
            parent=self.__maze.maze,
            position=self.__get_position(9, 8),
            size=self.__maze.cell_content_size,
            maze=self.__maze
        )

    def __new_clyde(self) -> Clyde:
        return Clyde(
            engine=self._engine,
            parent=self.__maze.maze,
            position=self.__get_position(3, 8),
            size=self.__maze.cell_content_size,
            maze=self.__maze
        )

    def __new_maze(self) -> Maze:
        return Maze(
            engine=self._engine,
            maze_generator=self.__maze_generator,
            parent=self.__maze_guide_wrapper,
            vertical_cells=VERTICAL_CELLS,
            horizontal_cells=HORIZONTAL_CELLS,
        )

    def __get_position(self, row: int, col: int) -> tuple[int, int]:
        return (
            row * self.__maze.cell_size + self.__maze.cell_border_size,
            col * self.__maze.cell_size + self.__maze.cell_border_size
        )

__all__ = ["InstructionsScene"]
