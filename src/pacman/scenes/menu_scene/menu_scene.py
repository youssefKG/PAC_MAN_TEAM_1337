from typing import override
from src.core import (
    ImageType,
    Engine,
)
from src.core import Key
from .menu import Menu, MenuButtonType
from src.pacman.scenes.base import BaseScene
from src.pacman.game_state import  GameStateManager, GameState

class MenuScene(BaseScene):
    def __init__(self, engine: Engine, game_state_manager: GameStateManager) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__container = (
            self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    position=(0, 0),
             ).set_parent().create()
        )
        self.__menu: Menu = Menu(
            parent=self.__container ,
            engine=self._engine,
            event_container=self._events_container,
        )
        self._events_container.add_event(key=Key.UP, callback=lambda: self.__menu.on_change(Key.UP))
        self._events_container.add_event(key=Key.DOWN, callback=lambda: self.__menu.on_change(Key.DOWN))
        self._events_container.add_event(key=Key.ENTER, callback=self.__change_scene)

    @override
    def mount(self) -> None:
        super().mount()
        self.__container.mount()

    @override
    def unmount(self) -> None:
        super().unmount()
        self.__container.unmount()

    def __change_scene(self) -> None:
        self.unmount()
        match self.__menu.active_button:
            case MenuButtonType.SETTINGS:
                self.__game_state_manager.change_state(GameState.SETTINGS)
            case MenuButtonType.PLAY:
                self.__game_state_manager.change_state(GameState.PLAY)
            case MenuButtonType.QUIT:
                self._engine.close_window()
            case MenuButtonType.HIGH_SCORES:
                self.__game_state_manager.change_state(GameState.HIGH_SCORES)
            case MenuButtonType.INSTRUCTIONS:
                self.__game_state_manager.change_state(GameState.INSTRUCTIONS)
