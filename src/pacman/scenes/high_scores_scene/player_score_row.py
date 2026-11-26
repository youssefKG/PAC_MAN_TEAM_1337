from uuid import uuid4
from src.core import Engine, PixelImage, ImageType, GridImage, RgbColors
from src.pacman.validation_models import PlayerScoreModel

RANK_IMAGE_WIDTH  =0.12
RANK_IMAGE_HEIGHT: float = 1.

class PlayerScoreRow:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage,
        player_score: PlayerScoreModel,
        rank: int,
        position: tuple[float | int, float | int],
    ) -> None:
        self.__rank: int = rank
        self.__id: str = str(uuid4())
        self.__player_score: PlayerScoreModel = player_score
        self.__parent: PixelImage = parent
        self.__engine: Engine = engine
        self.__position: tuple[float | int, float | int] = position
        self.__background_image: PixelImage  = (
            self.__engine.new_image(
                width=1.,
                height=0.09,
                image_type=ImageType.PIXEL_IMAGE,
                position=self.__position,
            ).set_parent(self.__parent).center_x().create()
        )
        self.__background_image.set_background_color(RgbColors.TRANSPARENT_GREEN)
        self.__badge: GridImage | PixelImage = self.__get_rank_image()
        self.__background_image.add_text(
            text=self.__engine.new_text(
                text=self.__player_score.name,
                font_size=20,
                lettere_spacing=1,
                color=RgbColors.WHITE,

            ).center_y(),
            position=(0.2, 0.5)
        )
        self.__background_image.add_text(
            text=self.__engine.new_text(
                text=str(self.__player_score.points),
                font_size=20,
                lettere_spacing=4,
                color=RgbColors.WHITE,

            ).center_y(),
            position=(0.8, 0.5)
        )
    def id(self) -> str:
        return self.__id

    def toggle_background(self) -> None:
        self.__background_image.toggle()

    def get_rank_badge(self) -> GridImage:
        return (
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

    def delete(self) -> None:
        self.__background_image.delete()

    def __get_rank_image(self) -> GridImage | PixelImage:
        rank_image: GridImage | PixelImage
        match self.__rank:
            case 0:
                rank_image = (
                    self.__engine.new_image(
                        width=RANK_IMAGE_WIDTH,
                        height=RANK_IMAGE_HEIGHT,
                        image_type=ImageType.GRID_IMAGE,
                        total_rows=8,
                        total_cols=10,
                        row=4,
                        col=9,
                        position=(.0, 0.5),
                        path="src/assests/badges/badges.png",
                    )
                    .set_parent(self.__background_image).
                    center_y()
                    .create()
                )
            case 1:
                rank_image =  (
                    self.__engine.new_image(
                        width=RANK_IMAGE_WIDTH,
                        height=RANK_IMAGE_HEIGHT,
                        image_type=ImageType.GRID_IMAGE,
                        total_rows=8,
                        total_cols=10,
                        row=3,
                        col=9,
                        position=(.0, 0.5),
                        path="src/assests/badges/badges.png",
                    )
                    .set_parent(self.__background_image).
                    center_y()
                    .create()
                )
            case 2:
                rank_image = (
                    self.__engine.new_image(
                        width=RANK_IMAGE_WIDTH,
                        height=RANK_IMAGE_HEIGHT,
                        image_type=ImageType.GRID_IMAGE,
                        total_rows=8,
                        total_cols=10,
                        row=2,
                        col=9,
                        position=(.0, 0.5),
                        path="src/assests/badges/badges.png",
                    )
                    .set_parent(self.__background_image).
                    center_y()
                    .create()
                )
            case _:
                rank_image = (
                        self.__engine.new_image(
                            image_type=ImageType.PIXEL_IMAGE,
                            width=RANK_IMAGE_WIDTH,
                            height=RANK_IMAGE_HEIGHT,
                            position=(.0, 0.5)
                        )
                    .set_parent(self.__background_image).center_y().create()
                )
                rank_image.add_text(
                        text=self.__engine.new_text(
                            text=str(self.__rank + 1),
                            font_size=30,
                            lettere_spacing=1,
                            color=RgbColors.WHITE
                        ).to_center(),
                        position=(0.5, 0.5)
                )
        return rank_image
