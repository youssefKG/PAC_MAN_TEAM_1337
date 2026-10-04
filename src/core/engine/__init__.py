import sys
from typing import Callable, cast
from typing_extensions import Self
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
from src.utils import Logger
 
class Engine:
    def __init__(self,
    ) -> None:
        self.__window_width: int
        self.__window_height: int
        self.__renderer: RendererType
        self.__image_factory: ImageFactory
        self.__elapsed_time: float
        self.__is_initialized: bool = False

    def __call__(
        self,
        window_width: int | None=None,
        window_height: int | None=None,
        title: str="Engine",
        monitor_size: bool = False
    ) -> Self:
        if self.__is_initialized:
            return self
        if monitor_size and (window_width is not None or window_height is not None):
            Logger.error(
                "window_width and window_height must not be" 
                +" provided when monitor_size is specified.",
                "ENGINE"
            )
            sys.exit(1)
        if not monitor_size and (window_width is None or window_height is not None):
            Logger.error(
                "indow_width and window_height must be provided "
                + "when monitor_size is not specified.",
                "Engine"
            )
            sys.exit(1)
        self.__renderer = Renderer(1, 1, title.encode("ASCII"), True)
        if monitor_size:
            self.__window_width, self.__window_height = get_monitor_size()
        else:
            self.__window_width, self.__window_height = cast(int, window_width), cast(int, window_height)
        set_window_size(self.__renderer, self.__window_width, self.__window_height)
        self.__elapsed_time = Clock()
        self.__renderer = Renderer(
            self.__window_width,
            self.__window_height,
            title.encode("ASCII"), 
            True
        )
        self.__image_factory = ImageFactory(self.__renderer)
        self.__is_initialized = True
        return self

    def new_image(
            self,
            /,
            *,
            width: int,
            height: int,
            image_format: ImageFormat=ImageFormat.PIXEL,
            frames: int = 1,
            path: str = "",
            time_per_frame: float = 0,
            col: int = 1,
            row: int = 1,
            total_colums: int = 1,
            total_rows: int = 1
        ) -> ImageInterface:
        return self.__image_factory(
            width=width,
            height=height,
            image_format=image_format,
            frames=frames,
            path=path,
            time_per_frame=time_per_frame
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

engine: Engine = Engine()
__all__ = ["engine", "Engine"]
