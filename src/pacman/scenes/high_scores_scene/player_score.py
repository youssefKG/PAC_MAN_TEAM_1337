from typing import cast
from uuid import uuid4
from src.core import Engine, PixelImage, ImageType, GridImage, RgbColors, PngImage

class PlayerScore:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        name: str,
        rank: int,
        parent: PngImage,
        position: tuple[float | int, float | int],
        is_visible: bool = False
    ) -> None:
        self.__id: str = str(uuid4())
        self.__name: str = name
        self.__rank: int = rank
        self.__parent: PngImage = parent
        self.__engine: Engine = engine
        self.__position: tuple[float | int, float | int] = position
        self.__is_visible: bool = is_visible
        self.__background_image: PixelImage  = cast(
            PixelImage,
            self.__engine.new_image(
                width=1.,
                height=.1,
                image_type=ImageType.PIXEL_IMAGE,
                is_visible=self.__is_visible,
                position=self.__position,
            ).set_parent(self.__parent).center_x().create()
        )
        self.__background_image.set_background_color(RgbColors.GREEN)
        self.__badge: GridImage = cast(
            GridImage,
            self.__engine.new_image(
                width=0.12,
                height=.9,
                image_type=ImageType.GRID_IMAGE,
                total_cols=10,
                total_rows=8,
                col=9,
                row=4 if rank == 0 else 7,
                path="src/assests/badges/badges.png",
                position=(.0, 0.5)
            )
            .set_parent(self.__background_image).center_y()
            .create()
        )
        self.__background_image.add_text(
            text=self.__engine.new_text(
                text=self.__name,
                font_size=20,
                lettere_spacing=4,
                color=RgbColors.WHITE,

            ).center_y(),
            position=(0.2, 0.5)
        )
    def id(self) -> str:
        return self.__id

    def toggle_background(self) -> None:
        self.__background_image.toggle()

    def get_rank_badge(self) -> GridImage:
        match self.__rank:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                ...
        return cast(
            GridImage,
            self.__engine.new_image(
                width=0.2,
                height=1.,
                image_type=ImageType.GRID_IMAGE,
                col=9,
                row=7,
                total_cols=10,
                total_rows=10,
                path="src/assets/badges/badges.png"
            ).set_parent(self.__background_image).create()
        )
