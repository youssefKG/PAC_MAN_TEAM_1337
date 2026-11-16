import os
from enum import Enum, auto
from src.pacman.validation_models import PlayerScoreModel, PlayerScoreRootModel
from src.pacman.config_parser import ConfigParser
from pydantic import ValidationError
from src.utils import Logger

class GameState(Enum):
    MENU = auto()
    PLAY = auto()
    SETTINGS = auto()
    SCORE = auto()
    QUIT = auto()
    HIGH_SCORES = auto()

HIGH_SCORES_PATH = "high_scores.json"

class GameStateManagerError(Exception):
    ...

class GameStateManager:
    def __init__(
        self,
        *,
        default_state: GameState = GameState.MENU,
        config_path: str = "config.json",
        # parser: ConfigParser
     ) -> None:
        self.__state: GameState = default_state
        self.__config_parser: ConfigParser = ConfigParser(config_path)
        self.__players_scores: list[PlayerScoreModel] = self.__load_high_scores_players()

    @property
    def state(self) -> GameState:
        return self.__state

    def change_state(self, new_state: GameState) -> None:
        self.__state = new_state

    def __load_high_scores_players(self) -> list[PlayerScoreModel]:
        try:
            if not os.access(HIGH_SCORES_PATH, os.F_OK):
                raise GameStateManagerError()
            elif not os.access(HIGH_SCORES_PATH, os.R_OK):
                raise GameStateManagerError()
            with open(HIGH_SCORES_PATH, "r") as file:
                players_scores: list[PlayerScoreModel] = PlayerScoreRootModel.model_validate_json(file.read()).root
                players_scores.sort(key=lambda player_score: player_score.points, reverse=True)
                return players_scores
        except ValidationError as error:
            raise GameStateManagerError(str(error))

    def save_high_scores_players(self) -> None:
        try:
            with open(HIGH_SCORES_PATH, "w") as high_scores_file:
                players_scores: str = PlayerScoreRootModel(self.__players_scores).model_dump_json(indent=4)
                _ = high_scores_file.write(players_scores)
        except Exception as error:
            Logger.error(str(error), "Game State Manager")

    @property
    def players_score(self) -> list[PlayerScoreModel]:
        return self.__players_scores
