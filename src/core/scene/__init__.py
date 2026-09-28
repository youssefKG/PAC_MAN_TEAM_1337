import src.core.image.base import Image
class Scene:
    def __init__(self) -> None:
        self.__images: list[Image] = list()
        pass


    def add_image(self, image: Image) -> None:
        self.__images.append(image)
        pass

    def render(self) -> None:
        pass


class Window:
    def __init__(self) -> None:
        self.__current_scene: Scene

