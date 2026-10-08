from typing import override, cast
from src.core import FrameImage, ImageType, GridImage, PngImage, PixelImage, RgbColors
from src.core import Vector2
from src.core import Scene, Engine
import random


class MenuScene(Scene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
        self.__transparent_background = cast(
                PixelImage,
                    self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    time_per_frame=10,
                    position=Vector2(x=0., y=0.),
              )
        )
        self.__transparent_background.set_background_color(RgbColors.BLACK)
        self.__transparent_background.to_window()
        self.__layout_image: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width= 1900,
                height=1400,
                image_type=ImageType.GRID_IMAGE,
                row=3,
                col=4,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/orange_border.png",
                position=Vector2(x=40., y=40.)
            )
        )
        self.__box_image2: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                image_type=ImageType.PIXEL_IMAGE,
                width=300,
                height=300,
                time_per_frame=10,
                position=Vector2(x=0., y=0.),
                parent=self.__layout_image)
        )
        self.__box_image2.set_background_color(RgbColors.RED)
        self.__boucing_spirits: list[PngImage] = self.__generate_bouncing_spirits(500)
        self.__velocity: list[Vector2] = self.__generate_random_velocities(500)
        self.__orange_ghost_image: FrameImage = cast(
            FrameImage,
            self._engine.new_image(
                width=100,
                height=100 ,
                frames=8,
                image_type=ImageType.FRAME_IMAGE,
                path="src/assests/orange_ghost.png",
                time_per_frame=0.5,
            )
        )

    @override
    def update(self, elapsed_time: float) -> None:
        self.__bouncings_images_animation(elapsed_time)
        self.__orange_ghost_image.move_to(
            target=Vector2(x=1000., y=300.),
            dt=elapsed_time,
            speed_per_frame_unit=35
        )
        self.__orange_ghost_image.update(elapsed_time)

    def __bouncings_images_animation(self, elapsed_time: float) -> None:
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

    def __generate_bouncing_spirits(self, total: int) -> list[PngImage]:
        return [cast(
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
            ) for _ in range(total)]

    def __generate_random_velocities(self, total: int) -> list[Vector2]:
        return [
            Vector2(
                x=float(random.choice([self.__window_width, -self.__window_width])),
                y=float(random.choice([self.__window_height, -self.__window_height]))
            ) for _ in range(total)
        ]


    def renderer(self) -> None:
        for spirit in self.__boucing_spirits:
             spirit.to_window()
        self.__layout_image.to_window()
        self.__box_image2.to_window()
        self.__orange_ghost_image.to_window()
