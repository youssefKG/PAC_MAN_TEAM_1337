from src.pacman.game_state import GameState, GameStateManager
from src.core import Engine

# ************ SCENES START ***************************
from src.pacman.scenes.common import Background
from src.pacman.scenes.base import BaseScene
from src.pacman.scenes.high_scores_scene import HighScoresScene
from src.pacman.scenes.instructions_scene import InstructionsScene
from src.pacman.scenes.menu_scene import MenuScene
from src.pacman.scenes.game_scene import GameScene
from src.pacman.scenes.settings_scene import SettingsScene
# ************ SCENES END ***************************


class SceneManager:
    def __init__(self, /, *, game_state_manager: GameStateManager, engine: Engine) -> None:
        self.__engine: Engine = engine
        self.__game_state_manager: GameStateManager = game_state_manager
        self.__menu_scene: MenuScene = MenuScene(self.__engine, self.__game_state_manager)
        self.__game_scene: GameScene = GameScene(self.__engine, self.__game_state_manager)
        self.__settings_scene: SettingsScene = SettingsScene(engine, self.__game_state_manager)
        self.__high_scores_scene: HighScoresScene = HighScoresScene(
            engine=self.__engine,
            game_state_manager=self.__game_state_manager
        )
        self.__background: Background = Background(self.__engine)
        self.__insructions_scene: InstructionsScene = InstructionsScene(
            engine=self.__engine,
            game_state_manager=self.__game_state_manager
        )
        self.__background.mount()

    def update(self, elapsed_time: float) -> None:
        self.__background.update(elapsed_time)
        match self.__game_state_manager.state:
            case GameState.MENU:
                self.__update_scene(self.__menu_scene, elapsed_time)
            case GameState.HIGH_SCORES:
                self.__update_scene(self.__high_scores_scene, elapsed_time)
            case GameState.INSTRUCTIONS:
                self.__update_scene(self.__insructions_scene, elapsed_time)
            case GameState.SETTINGS:
                self.__update_scene(self.__settings_scene, elapsed_time)
            case GameState.PLAY:
                self.__update_scene(self.__game_scene, elapsed_time)
            case _:
                ...

    def __update_scene(self, scene: BaseScene, elapsed_time: float) -> None:
        if not scene.is_visible:
            scene.mount()
        scene.update(elapsed_time)
