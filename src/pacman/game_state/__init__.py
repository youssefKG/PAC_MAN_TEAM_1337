from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    START = auto()
    WIN_LOSE = auto()
    HIGH_SCORE = auto()
    SETTINGS = auto()
    QUIT = auto()
    PLAY = auto()


class PacmanState:
    def __init__(self) -> None:
        self.__state: GameState = GameState.MENU

    def change(self, new_state: GameState) -> None:
        self.__state = new_state
