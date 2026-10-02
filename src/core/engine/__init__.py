from typing import Callable
from src.mlx.libmlx import  (
    Clock,
    set_window_size,
    Renderer,
    RendererType,
    loop,
    loop_hook,
    get_monitor_size
)
from src.core.image import ImageInterface, ImageFactory, ImageFormat
 
class Engine:
    def __init__(self,
         window_width: int=10,
         window_height: int = 10,
         title: str ="ENGINE"
    ) -> None:
        self.__window_width, self.__window_height = window_width, window_height
        self.__renderer: RendererType = Renderer(
            self.__window_width,
            self.__window_height,
            title.encode("ASCII"), 
            True
        )
        self.__image_factory: ImageFactory = ImageFactory(self.__renderer)
        self.__elapsed_time: float = Clock()

    def new_image(
            self,
            /,
            *,
            width: int,
            height: int,
            image_format: ImageFormat=ImageFormat.PIXEL,
            frames: int = 1,
            path: str = "",
        ) -> ImageInterface:
        return self.__image_factory(
            width=width,
            height=height,
            image_format=image_format,
            frames=frames,
            path=path
        )

    def set_window_to_monitor_size(self) -> None:
        self.__window_width, self.__window_height = get_monitor_size()
        set_window_size(self.__renderer, self.__window_width, self.__window_height)

    def game_loop(self, callback: Callable[[float], None]) -> None:
        self.__elapsed_time = Clock()
        loop_hook(self.__renderer, lambda _: callback(self.__elapsed_time))
        loop(self.__renderer)

    @property
    def window_dimension(self) -> tuple[int, int]:
        return self.__window_width, self.__window_height

__all__ = ["Engine"]
