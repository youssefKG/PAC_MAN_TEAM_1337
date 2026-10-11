from src.core import Engine

class BaseScene:
    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine
