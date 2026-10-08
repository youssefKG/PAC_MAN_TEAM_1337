import sys
from typing import Callable, cast
from src.core.image import BaseImage
from src.core.vector2 import Vector2
from typing_extensions import Self
from src.mlx.libmlx import  (
    set_window_size,
    Renderer,
    RendererType,
    loop,
    loop_hook,
    get_monitor_size,
    get_mouse_position,
)
from src.core.image import ImageFactory, ImageType
from src.utils import Logger
import time
 
class Engine:
    def __init__(self,
    ) -> None:
        self.__window_width: int
        self.__window_height: int
        self.__renderer: RendererType
        self.__image_factory: ImageFactory
        self.__elapsed_time: float
        self.__is_initialized: bool = False
        self.__current_time: float

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
        if not monitor_size and (window_width is None or window_height is None):
            print("monitor _size:" , monitor_size)
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
        self.__renderer = Renderer(
            self.__window_width,
            self.__window_height,
            title.encode("ASCII"), 
            True
        )
        self.__image_factory = ImageFactory(self.__renderer)
        self.__is_initialized = True
        self.__current_time = time.time()
        return self

    def new_image(
            self,
            /,
            *,
            width: int | float,
            height: int | float,
            image_type: ImageType=ImageType.PIXEL_IMAGE,
            frames: int = 1,
            path: str = "",
            time_per_frame: float = 0,
            col: int = 1,
            row: int = 1,
            total_cols: int = 1,
            total_rows: int = 1,
            parent: BaseImage | None = None,
            position: tuple[int | float, int | float] | None=None,
        ) -> BaseImage:
        return self.__image_factory(
            width=width,
            height=height,
            image_type=image_type,
            frames=frames,
            path=path,
            time_per_frame=time_per_frame,
            total_rows=total_rows,
            total_cols=total_cols,
            col=col,
            row=row,
            position=position,
            parent=parent
        )

    def set_window_to_monitor_size(self) -> None:
        self.__window_width, self.__window_height = get_monitor_size()
        set_window_size(self.__renderer, self.__window_width, self.__window_height)

    def game_loop(self, callback: Callable[[float], None]) -> None:
        loop_hook(self.__renderer, lambda _: self.__game_loop(callback))
        loop(self.__renderer)

    @property
    def window_dimension(self) -> tuple[int, int]:
        return self.__window_width, self.__window_height

    def get_mouse_position(self) -> Vector2:
        x, y = get_mouse_position(self.__renderer)
        return Vector2(x=x, y=y)

    def __game_loop(self, callback: Callable[[float], None]) -> None:
        elapsed_time = time.time() - self.__current_time
        self.__current_time = time.time()
        callback(elapsed_time)

engine: Engine = Engine()
__all__ = ["engine", "Engine"]
