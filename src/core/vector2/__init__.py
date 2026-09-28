import sys

from src.utils import Logger

class Vector2:
    def __init__(self, /, *, x: float, y: float) -> None:
        self.__x: float = x
        self.__y: float = y


    def translate_x(self, x: float) -> None:
        self.__x += x

    def translate_y(self, y: float) -> None:
        self.__y += y

    def move_to(self, position: "Vector2") -> None:
        self.__x = position.x
        self.__y = position.y

    def add(self, other: "Vector2") -> None:
        self.__x += other.x
        self.__y += other.y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x_value: int) -> None:
        self.__x = x_value

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y_value: int) -> None:
        self.__y = y_value



__all__ = ["Vector2"]
