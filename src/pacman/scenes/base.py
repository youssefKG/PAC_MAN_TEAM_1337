from src.core import Engine, EventContainer
from abc import ABC, abstractmethod

class BaseScene(ABC):
    def __init__(self, engine: Engine, is_visible: bool = False) -> None:
        self._engine: Engine = engine
        self._events_container: EventContainer = EventContainer()
        self._engine.add_events_container(self._events_container)
        self._is_visible: bool = is_visible

    @property
    def is_visible(self) -> bool:
        return self._is_visible

    @abstractmethod
    def mount(self) -> None:
        self._is_visible = True
        self._events_container.on()
        ...

    @abstractmethod
    def unmount(self) -> None:
        self._is_visible = False
        self._events_container.off()
        ...

    def update(self, elapsed_time: float) -> None:
        _ = elapsed_time
