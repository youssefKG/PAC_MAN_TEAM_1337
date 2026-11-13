from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    PLAY = auto()
    SETTINGS = auto()
    SCORE = auto()
    QUIT = auto()
    HIGH_SCORES = auto()

    
class GameStateManager:
    def __init__(self, default_state: GameState = GameState.MENU) -> None:
        self.__state: GameState = default_state

    @property
    def state(self) -> GameState:
        return self.__state


    def change_state(self, new_state: GameState) -> None:
        self.__state = new_state
