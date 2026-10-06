from src.mlx.libmlx import Image, RendererType, get_frames_of_images, image_to_window, resize_image
from .base import BaseImage, ImageType
from src.core.vector2 import Vector2

class FrameImage(BaseImage):
    def __init__(
        self,
        /, 
        *,
        renderer: RendererType,
        width: int,
        height: int,
        image_type: ImageType,
        path: str,
        time_per_frame: float,
        position: Vector2 | None,
        frames:  int = 1,
        z_index: int = 10,
    ) -> None:
        super().__init__(
            renderer=renderer,
            width=width,
            height=height,
            image_type=image_type,
            position=position
        )
        self._path: str = path
        self.__frames: int = frames
        self.__frames_image: list[Image] = get_frames_of_images(
            renderer=self._renderer,
            path=path,
            frames=self.__frames,
            width=self._width,
            height=self._height
        )
        self.__time_passed: float = 0.
        print(self.__frames)
        self.__current_frame_idx: int = 0
        self.__time_per_frame: float = time_per_frame

    def image_to_window(self) -> None:
        image_to_window(
            self._renderer,
            self.__frames_image[self.__current_frame_idx], int(self._position.x),
            int(self._position.y)
        )

    def to_window(self) -> None:
        for frame_image in self.__frames_image:
            frame_image.contents.enabled = False
            image_to_window(
                self._renderer,
                frame_image,
                int(self._position.y),
                int(self._position.x)
            )

    def update(self, elapsed_time: float) -> None:
        current_image: Image = self.__get_current_image
        if self.__time_passed >= self.__time_per_frame:
            current_image.contents.enabled = False
            if self.__current_frame_idx == len(self.__frames_image) - 1:
                self.__current_frame_idx = 0
            self.__current_frame_idx += 1
            current_image = self.__get_current_image
            current_image.contents.enabled = True
            self.__time_passed -= self.__time_per_frame
        self.__time_passed += elapsed_time
        current_image.contents.instances[0].x = int(self._position.x)
        current_image.contents.instances[0].y = int(self._position.y)

    @property
    def __get_current_image(self) -> Image:
        return self.__frames_image[self.__current_frame_idx]
