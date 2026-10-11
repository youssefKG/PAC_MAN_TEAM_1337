from enum import Enum, auto

class Event(Enum):
    CLICK = auto()
    MOUSE_MOVE = auto()
    KEY_DOWN = auto()

class EventHandler:
    def __init__(self) -> None:
        pass
