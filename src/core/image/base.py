from typing import cast
from src.utils import Logger
from uuid import uuid4
from typing import Protocol
from ..vector2 import Vector2


class ImageInterface(Protocol):
    def render(self) -> None:
        ...

    @property
    def id(self) -> str: ...


class ImageBase:
    def __init__(
        self, *,
        width: int,
        height: int,
        z_index: int=0,
        position: Vector2
    ) -> None:
        self.__id: str = str(uuid4())
        self.__z_index: int = z_index
        self.__width: int = width
        self.__height: int = height
        self.__childrens: list[ImageBase] = list()
        self.__parent: ImageBase | None = None
        self.__relative_position: Vector2 = position
        self.__absolute_position: Vector2 = self.__relative_position

    @property
    def id(self) -> str:
        return self.__id


    def add(self, image: "ImageBase", position: Vector2) -> None:
        self.__relative_position = position
        image.parent = self
        self.__childrens.append(image)

    @property
    def z_index(self) -> int:
        return self.__z_index


    def render(self) -> None:
        self.__update_absolute_position()
        if self.__parent is None:
            return
        else:
            pass
        self.__childrens.sort(key=lambda x: x.z_index, reverse=True)
        for child_image in self.__childrens:
            child_image.render()

    def set_parent(self, parent: "ImageBase") -> None:
        self.__parent = parent

    @property
    def relative_position(self) -> Vector2:
        return self.__relative_position
    
    def __update_absolute_position(self) -> None:
        current_parent: "ImageBase | None" = self.__parent
        while current_parent:
            self.__absolute_position.add(current_parent.relative_position)

    def put_center(self) -> None:
        pass

    @property
    def parent(self) -> "ImageBase | None":
        self.__update_absolute_position()
        return self.__parent

    @parent.setter
    def parent(self, other: "ImageBase") -> None: 
        self.__parent = other

# Test
if __name__ == "__main__":
    pass
