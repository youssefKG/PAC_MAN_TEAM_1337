from typing import override
from src.pacman.scenes.base import BaseScene
from src.core import (
    Engine,
    PixelImage,
    ImageType,
    Key
)
from src.pacman.game_state import GameState, GameStateManager

from src.mazegenerator import MazeGenerator
from src.pacman.scenes.common import Maze
from src.pacman.scenes.common import Pacman, Pinky, Blinky, Clyde, Direction
from .coins import Coin
from .heart import Heart

VERTICAL_CELLS = 16
HORIZONTAL_CELLS = 16


class GameScene(BaseScene):
    def __init__(self, engine: Engine, game_state_manager: GameStateManager) -> None:
        super().__init__(engine=engine)
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__scene_container: PixelImage = self.__new_scene_container()



        self.__maze_generator: MazeGenerator = MazeGenerator(
            size=(HORIZONTAL_CELLS, VERTICAL_CELLS)
        )
        self.__maze_generator.generate()
        self.__maze: Maze = self.__new_maze()
        self.__maze.draw()

        self.__pacman: Pacman = self.__new_pacman()
        self.__pinky: Pinky = self.__new_pinky()
        self.__blinky: Blinky = self.__new_blinky()
        self.__clyde: Clyde = self.__new_clyde()
        
        # coin image
        self.__coin_wrapper: PixelImage = self.__new_coin_wrapper()
        self.__coin: Coin = self.__new_coin()
        # heart image
        self.__heart_wrapper: PixelImage = self.__new_heart_wrapper()
        self.__heart: Heart = self.__new_heart()


        self.__set_events_to_events_container()
    @override
    def mount(self) -> None:
        super().mount()
        self.__scene_container.mount()

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__scene_container.unmount()

    @override
    def update(self, elapsed_time: float) -> None:
        self.__coin.update(elapsed_time)
        self.__heart.update(elapsed_time)
        self.__pacman.update(elapsed_time)
        self.__pinky.update(elapsed_time)
        self.__blinky.update(elapsed_time)
        self.__clyde.update(elapsed_time)

    def __new_scene_container(self) -> PixelImage:
        return self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=self.__window_width,
            height=self.__window_height,
            position=(0, 0),
        ).set_parent().create()

    def __new_maze(self) -> Maze:
        return Maze(
            engine=self._engine,
            maze_generator=self.__maze_generator,
            parent=self.__scene_container,
            vertical_cells=VERTICAL_CELLS,
            horizontal_cells=HORIZONTAL_CELLS,
        )

    def __new_heart_wrapper(self) -> PixelImage:
        return self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=.9,
            height=0.9,
            position=(.2, .10)
        ).set_parent(self.__scene_container).to_center().create()

    def __new_heart(self) -> Heart:
        return Heart(
            engine=self._engine,
            parent=self.__scene_container,
            position=self.__get_position(0, 2),
            size=int(self.__maze.cell_size)
        )
 
    def __new_coin_wrapper(self) -> PixelImage:
        return self._engine.new_image(
            image_type=ImageType.PIXEL_IMAGE,
            width=.9,
            height=0.9,
            position=(.2, .2)
        ).set_parent(self.__scene_container).to_center().create()

    def __new_coin(self) -> Coin:
        return Coin(
            engine=self._engine,
            parent=self.__scene_container,
            position=self.__get_position(0, 0),
            size=int(self.__maze.cell_size)
        )
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
 
    def __get_position(self, row: int, col: int) -> tuple[int, int]:
        return (
            row * self.__maze.cell_size + self.__maze.cell_border_size,
            col * self.__maze.cell_size + self.__maze.cell_border_size
        )

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

    def __set_events_to_events_container(self) -> None:
        self._events_container.add_event(key=Key.ESC, callback=lambda: self.__on_key_pressed(Key.ESC))
        self._events_container.add_event(key=Key.J, callback=lambda: self._engine.close_window())

        # **************************** PACMAN MOVEMENT START ******************************************
        self._events_container.add_event(key=Key.W, callback=lambda: self.__pacman.change_direction(Direction.UP))
        self._events_container.add_event(key=Key.A, callback=lambda: self.__pacman.change_direction(Direction.LEFT))
        self._events_container.add_event(key=Key.S, callback=lambda: self.__pacman.change_direction(Direction.DOWN))
        self._events_container.add_event(key=Key.D, callback=lambda: self.__pacman.change_direction(Direction.RIGHT))
        self._events_container.add_event(key=Key.UP, callback=lambda: self.__pacman.change_direction(Direction.UP))
        self._events_container.add_event(key=Key.LEFT, callback=lambda: self.__pacman.change_direction(Direction.LEFT))
        self._events_container.add_event(key=Key.DOWN, callback=lambda: self.__pacman.change_direction(Direction.DOWN))
        self._events_container.add_event(key=Key.RIGHT, callback=lambda: self.__pacman.change_direction(Direction.RIGHT))
        # **************************** PACMAN MOVEMENT END ******************************************


