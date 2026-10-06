from typing import override, cast
from src.core import FrameImage, ImageType, GridImage, PngImage
from src.core import Vector2
from src.core import Scene, Engine
import random


class MenuScene(Scene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
        self.__spinners: list[PngImage] = [
                cast(
                PngImage,
                cast(
                    object,
                    self._engine.new_image(
                        image_type=ImageType.PNG_IMAGE,
                        width=16,
                        height=16,
                        path=random.choice(
                                [
                                    "src/assests/ghost_static.png",
                                    "src/assests/blue_ghost_static.png",
                                    "src/assests/pacman_static.png"
                                ]
                        ),
                        time_per_frame=10,
                        position=Vector2(
                            x=random.randrange(0, self.__window_width),
                            y=random.randrange(0, self.__window_height)
                        )
                    )
               )
            ) for _ in range(550)]

        self.__orange_ghost_image: FrameImage = cast(
            FrameImage,
            cast(
                object, self._engine.new_image(
                    width=100,
                    height=100 ,
                    frames=8,
                    image_type=ImageType.FRAME_IMAGE,
                    path="src/assests/orange_ghost.png",
                    time_per_frame=5,
                )
             )
        )
        self.__orange_ghost_image.to_window()
        layout_image2: GridImage = cast(GridImage, cast(object, self._engine.new_image(
                width= 900,
                height=900,
                image_type=ImageType.GRID_IMAGE,
                row=1,
                col=1,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/orange_border.png",
                position=Vector2(x=900, y=900)
        )))
        layout_image2.to_window()
        self.__velocity: list[Vector2] = [
            Vector2(
                x=float(random.choice([self.__window_width, -self.__window_width])),
                y=float(random.choice([self.__window_height, -self.__window_height]))
            ) for _ in self.__spinners
        ]
              
    @override
    def update(self, elapsed_time: float) -> None:
        for idx, spinner in enumerate(self.__spinners):
            if (spinner.position == self.__velocity[idx]):
                self.__velocity[idx].x = random.randrange(-self.__window_width, self.__window_width)
            if spinner.position.y + spinner.height >= self.__window_height or spinner.position.y <= 0:
                self.__velocity[idx].y = -self.__velocity[idx].y
            if spinner.position.x + spinner.width >= self.__window_width or spinner.position.x <= 0:
                self.__velocity[idx].x = -self.__velocity[idx].x
            spinner.move_to(
                target=self.__velocity[idx],
                dt=elapsed_time,
                speed_per_frame_unit=100
            )
            spinner.update(elapsed_time)
        self.__orange_ghost_image.move_to(target=Vector2(x=1000., y=300.), dt=elapsed_time, speed_per_frame_unit=3)
        self.__orange_ghost_image.update(elapsed_time)


    def bouncings_images_animation(self) -> None:
        pass
    def renderer(self) -> None:
        for spinner in self.__spinners:
             spinner.to_window()
