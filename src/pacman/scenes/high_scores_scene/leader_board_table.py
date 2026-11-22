from typing import  cast, Annotated
from src.core import (
    Engine,
    ImageType,
    PixelImage,
    GridImage,
    RgbColors,
    PngImage,
)
from .player_score_row import PlayerScoreRow
from src.pacman.game_state import GameStateManager
from src.pacman.validation_models import PlayerScoreModel
from .players_leaderboard_table_header import PlayersLeaderboardTableHeader

TOTAL_ROWS: int = 11
PLAYER_SCORE_ROW_HEIGHT: float = 1 / TOTAL_ROWS

class PlayersLeaderboardRows:
    def __init__(self, engine: Engine, players_score: list[PlayerScoreModel], parent: PixelImage) -> None:
        self.__players_score: list[PlayerScoreModel] = players_score[:10]
        self.__engine: Engine = engine
        self.__players_scores_ui: dict[Annotated[str, "player id"], PlayerScoreRow] = dict()
        self.__parent: PixelImage = parent

    def update(self, new_players_scores: list[PlayerScoreModel] | None = None) -> None:
        if new_players_scores:
            self.__players_score = new_players_scores
        # TODO: update the players scores

    def render(self) -> None:
        for rank, player_score in enumerate(self.__players_score):
            self.__players_scores_ui[player_score.id] = PlayerScoreRow(
                engine=self.__engine,
                player_score=player_score,
                position=(.5,  (PLAYER_SCORE_ROW_HEIGHT + PLAYER_SCORE_ROW_HEIGHT * rank)),
                rank=rank,
                parent=self.__parent
            )
    def delete(self) -> None:
        for player_score in self.__players_scores_ui.values():
            player_score.delete()


class LeaderBoardTable:
    def __init__(
        self,
        engine: Engine,
        parent: PixelImage,
        game_state_manager: GameStateManager
    ) -> None:
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__engine: Engine = engine
        self.__parent: PixelImage = parent
        self.__leaderboard: GridImage = cast(
            GridImage, 
            self.__engine.new_image(
                width=.35,
                height=0.64,
                image_type=ImageType.GRID_IMAGE,
                total_rows=4,
                total_cols=5,
                col=2,
                row=3,
                path="src/assests/menu/green_menu.png",
                position=(0.5, .25)
            )
            .set_parent(self.__parent)
            .center_x()
            .create()
        )
        self.__leaderboard_panel: PngImage = cast(
            PngImage,
            self.__engine.new_image(
                width=.4,
                height=.1,
                image_type=ImageType.PNG_IMAGE,
                path="src/assests/banner.png",
                position=(0.5, -.084),
            )
            .set_parent(self.__leaderboard).center_x().create()
        )
        self.__leaderboard_panel.add_text(
            text=self.__engine.new_text(
                    text="LEADERBOARD",
                    font_size=24,
                    lettere_spacing=4,
                    color=RgbColors.WHITE,
            )
            .to_center(),
            position=(0.5, 0.5)
        )
        self.__wood_background: PngImage = cast(
            PngImage,
            self.__engine.new_image(
                image_type=ImageType.PNG_IMAGE,
                width=.762,
                height=.75,
                position=(.494, .5),
                path="src/assests/backgrounds/wood_background.png"
            )
            .set_parent(self.__leaderboard)
            .to_center()
            .create()
        )
        self.__black_transparent_background: PixelImage = cast(
           PixelImage,
           self.__engine.new_image(
               width=1.,
               height=1.,
               image_type=ImageType.PIXEL_IMAGE,
               position=(.0, .0)
           )
          .set_parent(self.__wood_background)
          .create()
        )
        self.__black_transparent_background.set_background_color(RgbColors.BLACK_TRANS)
        self.__players_score_header_table: PlayersLeaderboardTableHeader = PlayersLeaderboardTableHeader(
                engine=self.__engine,
                parent=self.__black_transparent_background
        )
        self.__players_score_rows: PlayersLeaderboardRows =  PlayersLeaderboardRows(
            engine=self.__engine,
            players_score=self.__game_state_manager.players_score,
            parent=self.__black_transparent_background
        )
        self.__players_score_rows.render()
