from typing import cast
from src.core import Engine, ImageType, PixelImage, PngImage, Vector2, RgbColors, GridImage
import random

TOTAL_SPIRITS = 190

class Background:
    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = self._engine.window_dimension
        self.__boucing_spirits: list[PngImage] = self.__generate_bouncing_spirits(TOTAL_SPIRITS)
        self.__velocity: list[Vector2] = self.__generate_random_velocities(TOTAL_SPIRITS)
        self.__background_image = cast(
                PngImage,
                    self._engine.new_image(
                    image_type=ImageType.PNG_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    position=(0, 0),
                    path="src/assests/backgrounds/cenote_light_beam.png",
              ).set_parent().create()
        )
        self.__black_transparent_background = cast(
                PixelImage,
                    self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=self.__window_width,
                    height=self.__window_height,
                    position=(0, 0),
              ).set_parent().create()
        )
        self.__black_transparent_background.set_background_color(RgbColors.BLACK_TRANS)
        self.__banner: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width= 0.3,
                    height=0.1,
                    image_type=ImageType.GRID_IMAGE,
                    row=5,
                    col=4,
                    total_cols=5,
                    total_rows=8,
                    path="src/assests/15.png",
                    position=(.50, .0)
                )
                .set_parent(self.__black_transparent_background)
                .center_x()
                .create()
        )
        self.__banner.add_text(
            self._engine.new_text(
                text="PACMAN 42 PARIS",
                font_size=40,
                lettere_spacing=7,
                color=RgbColors.WHITE
            ).to_center(),
            (.5, 0.5)
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


    def mount(self) -> None:
        self.__background_image.mount()
        for spirit in self.__boucing_spirits:
             spirit.mount()
        self.__black_transparent_background.mount()
