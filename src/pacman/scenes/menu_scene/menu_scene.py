from typing import override, cast
from src.core import (
    FrameImage,
    ImageType,
    GridImage,
    PngImage,
    PixelImage,
    RgbColors,
    Engine,
    Scene,
    Vector2,
)
import random


TOTAL_SPIRITS = 80

class MenuScene(Scene):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)
        self.__window_width: int
        self.__window_height: int
        self.__window_width, self.__window_height = engine.window_dimension
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
        # self.__transparent_background.set_background_color(RgbColors.BLACK)
        self.__transparent_background.add_text(
            self._engine.new_text(
                text="PACMAN 1337",
                font_size=55,
                lettere_spacing=3,
                color=RgbColors.WHITE
            ).center_x(),
            (.5, 0.01)
        )
        self.__layout_image: GridImage = cast(
            GridImage,
            self._engine.new_image(
                width= .35,
                height=.40,
                image_type=ImageType.GRID_IMAGE,
                row=3,
                col=4,
                total_cols=5,
                total_rows=4,
                path="src/assests/menu/green_menu.png",
                position=(.5, .5),
            )
            .set_parent(self.__transparent_background)
            .to_center().create()
        )
        self.__box_image2: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__layout_image)
                .to_center().create()
        )
        self.__box_image2.set_background_color(RgbColors.GREEN)
        self.__settings: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width=.8,
                    height=.2,
                    image_type=ImageType.GRID_IMAGE,
                    row=3,
                    col=4,
                    total_cols=5,
                    total_rows=4,
                    path="src/assests/menu/green_menu.png",
                    position=(0.5, 0.2)
                ).set_parent(self.__box_image2).to_center().create()
        )
        self.__box_image: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__settings)
                .to_center().create()
        )
        self.__box_image.set_background_color(RgbColors.BLACK)
        self.__box_image.add_text(self._engine.new_text(text="Settings", lettere_spacing=3, font_size=22, color=RgbColors.WHITE).to_center(), position=(0.5, 0.5))
        self.__play_button: GridImage = cast(
                GridImage,
                self._engine.new_image(
                    width=.8,
                    height=.2,
                    image_type=ImageType.GRID_IMAGE,
                    row=3,
                    col=4,
                    total_cols=5,
                    total_rows=4,
                    path="src/assests/menu/green_menu.png",
                    position=(0.5, 0.42)
                ).set_parent(self.__box_image2).to_center().create()
        )
        self.__box_image3: PixelImage = cast(
                PixelImage,
                 self._engine.new_image(
                    image_type=ImageType.PIXEL_IMAGE,
                    width=.7,
                    height=.7,
                    time_per_frame=10,
                    position=(.5, .5),
                )
                .set_parent(self.__play_button)
                .to_center().create()
        )
        self.__box_image3.set_background_color(RgbColors.BLACK)
        self.__box_image3.add_text(self._engine.new_text(text="Play", lettere_spacing=3, font_size=22, color=RgbColors.WHITE).to_center(), position=(0.5, 0.5))
        self.__boucing_spirits: list[PngImage] = self.__generate_bouncing_spirits(TOTAL_SPIRITS)
        self.__velocity: list[Vector2] = self.__generate_random_velocities(TOTAL_SPIRITS)
        self.__orange_ghost_image: FrameImage = cast(
            FrameImage,
            self._engine.new_image(
                width=.03,
                height=.05,
                frames=8,
                image_type=ImageType.FRAME_IMAGE,
                path="src/assests/orange_ghost.png",
                time_per_frame=.17,
                position=(0, 0)
            ).set_parent(self.__box_image2).create()
        )
        self.__pacman: FrameImage = cast(
            FrameImage,
            self._engine.new_image(
                width=.03,
                height=.05,
                frames=8,
                image_type=ImageType.FRAME_IMAGE,
                path="src/assests/PacMan.png",
                time_per_frame=.17,
                position=(0, 0)
            ).set_parent(self.__box_image2).create()
        )

    @override
    def update(self, elapsed_time: float) -> None:
        self.__bouncings_images_animation(elapsed_time)
        orange_ghost_target = Vector2(x=self.__box_image2.position.x, y=self.__box_image2.position.y)
        orange_ghost_target.add(Vector2(x=self.__box_image2.width - self.__orange_ghost_image.width, y=0.))
        if self.__orange_ghost_image.position.x != orange_ghost_target.x:
            self.__orange_ghost_image.move_to(
                target=orange_ghost_target,
                dt=elapsed_time,
                speed_per_frame_unit=25,
            )
            self.__orange_ghost_image.update(elapsed_time)
        pacman_target = Vector2(x=self.__box_image2.position.x, y=self.__box_image2.position.y)
        pacman_target.add(Vector2(y=self.__box_image2.height - self.__pacman.height, x=0.))
        if self.__pacman.position.y != pacman_target.y:
            self.__pacman.move_to(
                target=pacman_target,
                dt=elapsed_time,
                speed_per_frame_unit=25
            )
            self.__pacman.update(elapsed_time)

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
                    ).set_parent(self.__box_image2).create()
            ) for _ in range(total)]

    def __generate_random_velocities(self, total: int) -> list[Vector2]:
        return [
            Vector2(
                x=float(random.choice([self.__window_width, -self.__window_width])),
                y=float(random.choice([self.__window_height, -self.__window_height]))
            ) for _ in range(total)
        ]


    def renderer(self) -> None:
        self.__transparent_background.to_window()
        for spirit in self.__boucing_spirits:
             spirit.to_window()
        self.__layout_image.to_window()
        self.__box_image2.to_window()
        self.__settings.to_window()
        self.__box_image.to_window()
        self.__play_button.to_window()
        self.__box_image3.to_window()
        self.__orange_ghost_image.to_window()
        self.__pacman.to_window()
