from typing import cast
from src.core import Engine, ImageType, PixelImage, PngImage, Vector2
import random

TOTAL_SPIRITS = 90

class BouncingSpirits:
    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__boucing_spirits: list[PngImage] = self.__generate_bouncing_spirits(TOTAL_SPIRITS)
        self.__velocity: list[Vector2] = self.__generate_random_velocities(TOTAL_SPIRITS)
        self.__transparent_background = cast(
                PngImage,
                    self._engine.new_image(
                    image_type=ImageType.PNG_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    position=(0, 0),
                    path="src/assests/backgrounds/cenote_light_beam.png",
              ).set_parent().create()
        )
    
    def __generate_random_velocities(self, total: int) -> list[Vector2]:
        return [
            Vector2(
                x=float(random.choice([self.__window_width, -self.__window_width])),
                y=float(random.choice([self.__window_height, -self.__window_height]))
            ) for _ in range(total)
        ]

    def __generate_bouncing_spirits(self, total: int) -> list[PngImage]:
        return [
                cast(
                    PngImage,
                    self._engine.new_image(
                        image_type=ImageType.PNG_IMAGE,
                        width=18,
                        height=18,
                        path=random.choice(
                            [
                                "src/assests/ghost_static.png",
                                "src/assests/blue_ghost_static.png",
                                "src/assests/pacman_static.png"
                            ]
                        ),
                        time_per_frame=10,
                        position=(
                            random.randrange(0, self.__window_width),
                            random.randrange(0, self.__window_height)
                        ),
                    ).set_parent().create()
            ) for _ in range(total)]


    def update(self, elapsed_time: float) -> None:
        for idx, spirit in enumerate(self.__boucing_spirits):
            if (spirit.position == self.__velocity[idx]):
                self.__velocity[idx].x = random.randrange(-self.__window_width, self.__window_width)
            if spirit.position.y + spirit.height >= self.__window_height or spirit.position.y <= 0:
                self.__velocity[idx].y = -self.__velocity[idx].y
            if spirit.position.x + spirit.width >= self.__window_width or spirit.position.x <= 0:
                self.__velocity[idx].x = -self.__velocity[idx].x
            spirit.move_to(
                target=self.__velocity[idx],
                dt=elapsed_time,
                speed_per_frame_unit=100
            )
            spirit.update(elapsed_time)


    def renderer(self) -> None:
        self.__transparent_background.to_window()
        for spirit in self.__boucing_spirits:
             spirit.to_window()
