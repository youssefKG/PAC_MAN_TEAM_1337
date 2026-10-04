from enum import Enum, auto

class GameState(Enum):
    Menu = auto()
    START = auto()
    WIN_LOSE = auto()
    HIGH_SCORE = auto()
