from typing import override
from src.core import Scene, Engine

class MenuScene(Scene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    @override
    def update(self, elapsed_time: float) -> None:
        pass
