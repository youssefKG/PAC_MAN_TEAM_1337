from enum import Enum, auto


class FSMJson(Enum):
    IN_START = auto()
    IN_JSON = auto()
    IN_STRING = auto()
    IN_COMMENT = auto()
    IN_END = auto()



