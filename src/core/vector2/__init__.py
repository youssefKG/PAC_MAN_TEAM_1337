import sys

from typing import override
from src.utils import Logger
import math

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
    def x(self, x_value: float) -> None:
        self.__x = x_value

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y_value: float) -> None:
        self.__y = y_value

    @override
    def __eq__(self, vector: object) -> bool:
        return isinstance(vector, Vector2) and vector.x == self.__x and vector.y == self.__y


    def magnitude(self, vector: 'Vector2 | None'=None) -> float:
        if vector is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)
        return math.sqrt((vector.x - self.__x) ** 2 + (vector.y - self.__y) ** 2)

    def normalize(self) -> 'Vector2':
        magnitude: float = self.magnitude()
        return Vector2(x=self.__x / magnitude, y=self.__y / magnitude)
    
    def sub(self, vector: 'Vector2') -> 'Vector2':
        return Vector2(x=vector.x - self.__x, y=vector.y - self.__y)

    @override
    def __str__(self) -> str:
        return f"x={self.__x}, y={self.__y}"

__all__ = ["Vector2"]
