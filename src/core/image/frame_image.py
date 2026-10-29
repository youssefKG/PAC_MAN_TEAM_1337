from typing import override
from typing_extensions import Self
from src.mlx.libmlx import Image, RendererType, get_frames_of_images, image_to_window, toggle_image, hide_image, display_image, hide_image
from .base import BaseImage, ImageType
from src.core.vector2 import Vector2
from src.core.event import EventHandler

class FrameImage(BaseImage):
    def __init__(
        self,
        /, 
        *,
        renderer: RendererType,
        event_handler: EventHandler,
        width: int | float,
        height: int | float,
        image_type: ImageType,
        path: str,
        time_per_frame: float,
        position: tuple[int | float, int | float] | None,
        frames:  int = 1,
        z_index: int = 10,
    ) -> None:
        super().__init__(
            renderer=renderer,
            event_handler=event_handler,
            width=width,
            height=height,
            image_type=image_type,
            position=position,
        )
        self._path: str = path
        self.__frames: int = frames
        self.__frames_image: list[Image]
        self.__time_passed: float = 0.
        self.__current_frame_idx: int = 0
        self.__time_per_frame: float = time_per_frame
        self.__is_hidden: bool = False


    @override
    def create(self) -> Self:
        self.__frames_image = get_frames_of_images(
            renderer=self._renderer,
            path=self._path,
            frames=self.__frames,
            width=self._width,
            height=self._height
        )
        return self


    @override
    def mount(self) -> None:
        if not self._has_been_in_window:
            for frame_image in self.__frames_image:
                image_to_window(
                    self._renderer,
                    frame_image,
                    int(self._position.y),
                    int(self._position.x)
                )
        else:
            display_image(self.__frames_image[self.__current_frame_idx])
            self.__is_hidden = True

    @override
    def unmount(self) -> None:
        hide_image(self.__frames_image[self.__current_frame_idx])
        self.__is_hidden = True

    def update(self, elapsed_time: float) -> None:
        if not self.__is_hidden:
            current_image: Image = self.__get_current_image
            if self.__time_passed >= self.__time_per_frame:
                hide_image(current_image)
                if self.__current_frame_idx == len(self.__frames_image) - 1:
                    self.__current_frame_idx = 0
                self.__current_frame_idx += 1
                current_image = self.__get_current_image
                display_image(current_image)
                self.__time_passed -= self.__time_per_frame
            self.__time_passed += elapsed_time
            current_image.contents.instances[0].x = int(self._position.x)
            current_image.contents.instances[0].y = int(self._position.y)

    @property
    def __get_current_image(self) -> Image:
        return self.__frames_image[self.__current_frame_idx]
