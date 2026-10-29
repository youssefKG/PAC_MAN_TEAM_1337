from src.core import Engine, EventContainer

class BaseScene:
    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine
        self._events_container: EventContainer = EventContainer()
        self._engine.add_events_container(self._events_container)
