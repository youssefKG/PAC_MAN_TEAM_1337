from typing import override
from typing_extensions import Self
from src.mlx.libmlx import (
    Image,
    RendererType,
    get_frames_of_images,
    image_to_window,
    hide_image,
    display_image,
    delete_image
)
from .base import BaseImage, ImageType

class FrameImage(BaseImage):
    def __init__(
        self,
        /, 
        *,
        renderer: RendererType,
        width: int | float,
        height: int | float,
        image_type: ImageType,
        path: str,
        time_per_frame: float,
        position: tuple[int | float, int | float] | None,
        frames:  int = 1,
        is_visible: bool
    ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            position=position,
            is_visible=is_visible
        )
        self._path: str = path
        self.__total_frames: int = frames
        self.__frames_image: list[Image]
        self.__time_passed: float = 0.
        self.__current_frame_idx: int = 0
        self.__time_per_frame: float = time_per_frame
        self.__is_hidden: bool = False
        self.__has_been_on_screen: bool = False


    @override
    def create(self) -> Self:
        self.__frames_image = get_frames_of_images(
            renderer=self._renderer,
            path=self._path,
            frames=self.__total_frames,
            width=self._width,
            height=self._height
        )
        return self

    @override
    def mount(self) -> None:
        if not self.__has_been_on_screen:
            for idx, frame_image in enumerate(self.__frames_image):
                if idx != 0:
                    hide_image(frame_image)
                image_to_window(
                    self._renderer,
                    frame_image,
                    int(self._position.y),
                    int(self._position.x)
                )
                self.__has_been_on_screen = True
        

    @override
    def unmount(self) -> None:
        hide_image(self.__frames_image[self.__current_frame_idx])
        self.__is_hidden = True

    def update(self, elapsed_time: float) -> None:
        if self.__time_passed >= self.__time_per_frame:
            hide_image(self.__frames_image[self.__current_frame_idx])
            display_image(self.__frames_image[(self.__current_frame_idx + 1) % self.__total_frames])
            self.__current_frame_idx = (self.__current_frame_idx + 1) % self.__total_frames
            self.__time_passed = .0
            self.__frames_image[self.__current_frame_idx].contents.instances[0].x = int(self._position.x)
            self.__frames_image[self.__current_frame_idx].contents.instances[0].y = int(self._position.y)
        self.__time_passed += elapsed_time
     
    @property
    def __get_current_image(self) -> Image:
        return self.__frames_image[self.__current_frame_idx]

    @override
    def delete(self) -> None:
        if self._parent is not None:
            self._parent.delete_children(self.id)
        for frame_img in self.__frames_image:
            hide_image(frame_img)
            delete_image(self._renderer, frame_img)
