from enum import Enum, auto
from src.mlx.libmlx import RendererType, key_hook, mlx, is_key_pressed
from typing import Callable, Annotated 
from uuid import uuid4

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
    KEY_ENTER           = 257

class EventContainer:
    def __init__(self) -> None:
        self.__id: str = str(uuid4)
        self.__is_on: bool = False
        self.__events_handlers: dict[Annotated[int, "event key"], Callable[[], None]] = dict()

    def on(self) -> None:
        self.__is_on = True

    def off(self) -> None:
        self.__is_on = False

    def run(self, key: int) -> None:
        if self.__is_on:
            if key in self.__events_handlers:
                self.__events_handlers[key]()

    def add_event(self, *, key: Key, callback: Callable[[], None]) -> None:
        self.__events_handlers[key.value] = callback

    def __bool__(self) -> bool:
        return self.__is_on

class EventHandler:
    def __init__(self, renderer: RendererType) -> None:
        self.__renderer: RendererType = renderer
        self.__events_containers: list[EventContainer] = list()

    def receive(self) -> None:
        key_hook(self.__renderer, self.__receive)

    def __receive(self, event_key: int) -> None:
        if is_key_pressed(self.__renderer, event_key):
            for events_container in self.__events_containers:
                if events_container:
                    events_container.run(event_key)

    def add_container(self, container: EventContainer) -> None:
        print("a container being added")
        self.__events_containers.append(container)

__all__ = ["EventHandler"]
