from src.core.scene import Scene
from src.core import Engine


class GameScene(Scene):

    def __init__(self, engine: Engine) -> None:
        super().__init(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension

        self.
        
    @override
    def update(self, elapsed_time: float) -> None:
           
        pass

    def renderer(self) -> None:
        pass

