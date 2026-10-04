from src.core import Engine, ImageInterface

class BaseScene:
    def __init__(self, engine: Engine) -> None:
        self.__engine: Engine = engine
