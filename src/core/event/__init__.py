from enum import Enum, auto
from src.mlx.libmlx import RendererType, key_hook
from typing import Callable
from collections import defaultdict

class Event(Enum):
    CLICK = auto()
    MOUSE_MOVE = auto()
    KEY_DOWN = auto()
    HOVER = auto()


class Key(Enum):
    KEY_I               = 73
    KEY_J               = 74
    KEY_K               = 75
    KEY_L               = 76


class Listener:
    def __init__(self, callback: Callable[[], None]) -> None:
        self.is_on: bool = True
        self.callback: Callable[[], None] = callback


class EventHandler:
    def __init__(self, renderer: RendererType) -> None:
        self.__renderer: RendererType = renderer
        self.__listeners: dict[int, dict[str, Listener]] =defaultdict(dict)

    def receive(self) -> None:
        key_hook(self.__renderer, self.__receive)

    def __receive(self, event_key: int) -> None:
        print(event_key)
        if event_key in self.__listeners:
            for id, listener in self.__listeners[event_key].items():
                if listener.is_on:
                    listener.callback()
                    print(id)

    def add_event(self, id: str, key: Key, callback: Callable[[], None]) -> None:
        self.__listeners[key.value][id]= Listener(callback)

    def off(self, key: Key, id: str) -> None:
        self.__listeners[key.value][id].is_on = False
        
    def on(self, key: Key, id: str) -> None:
        self.__listeners[key.value][id].is_on = True



__all__ = ["EventHandler"]
