from typing import cast
from src.pacman.scenes import MenuScene
from src.core import (
    Engine,
    engine,
    PixelImage,
    RgbColors,
    Vector2,
    FrameImage, 
    ImageType,
    GridImage,
    
)

class Pacman:
    def __init__(
        self,
     ) -> None:
        self.__engine: Engine = engine(monitor_size=True, title="PACMAN")
        self.__menu_scene: MenuScene = MenuScene(engine)
        self.__menu_scene.renderer()
        # self.__box_image: PixelImage = cast(
        #     PixelImage, self.__engine.new_image(
        #         width=IMAGE_WIDTH,
        #         height=IMAGE_HEIGHT,
        #         image_type=ImageType.PIXEL_IMAGE
        #     )
        # )
        # layout_image: GridImage = cast(GridImage, cast(object, self.__engine.new_image(
        #         width= 500,
        #         height=500,
        #         image_type=ImageType.GRID_IMAGE,
        #         row=2,
        #         col=2,
        #         total_cols=5,
        #         total_rows=4,
        #         path="src/assests/menu/orange_border.png"
        # )))
        # layout_image.to_window()
        # self.__box_image.to_window()
        # self.__box_image.set_background_color(RgbColors.PINK)
        # self.__orange_ghost_image: FrameImage = cast(
        #     FrameImage,
        #     cast(
        #         object, self.__engine.new_image(
        #             width=400,
        #             height=400 ,
        #             frames=7,
        #             image_type=ImageType.FRAME_IMAGE,
        #             path="src/assests/orange_ghost.png",
        #             time_per_frame=2,
        #         )
        #      )
        # )
        # self.__orange_ghost_image.to_window()
        # layout_image2: GridImage = cast(GridImage, cast(object, self.__engine.new_image(
        #         width= 900,
        #         height=900,
        #         image_type=ImageType.GRID_IMAGE,
        #         row=1,
        #         col=1,
        #         total_cols=5,
        #         total_rows=4,
        #         path="src/assests/menu/orange_border.png",
        #         position=Vector2(x=900, y=900)
        # )))
        # layout_image2.to_window()

    def run(self) -> None:
        self.__engine.game_loop(self.__update)


    def __update(self, elapsed_time: float) -> None:
        self.__menu_scene.update(elapsed_time)
        # self.__orange_ghost_image.move_to(
        #     target=Vector2(x=2000.0, y=30.0),
        #     dt=elapsed_time,
        #     speed_per_frame_unit=3
        # )
        # self.__box_image.move_to(
        #     target=Vector2(x=1000, y=1000),
        #     dt=elapsed_time,
        #     speed_per_frame_unit=13
        # )
        # self.__orange_ghost_image.update(elapsed_time)
        # self.__box_image.update(elapsed_time)

__all__ = ["Pacman"]
