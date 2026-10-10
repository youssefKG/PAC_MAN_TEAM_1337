from src.mlx.libmlx import (
    RendererType,
)


# Images
from .pixel_image import PixelImage
from .grid_image import GridImage
from .frame_image import FrameImage
from .base import ImageType, BaseImage
from .png_image import PngImage

_DEFAULT_IMAGE_WIDTH = 100

_DEFAULT_IMAGE_HEIGHT = 100

class ImageFactory:
    def __init__(self, renderer: RendererType) -> None:
        self.__renderer: RendererType = renderer

    def __call__(self,
            image_type: ImageType=ImageType.PIXEL_IMAGE,
            width: int | float=_DEFAULT_IMAGE_WIDTH,
            height: int | float = _DEFAULT_IMAGE_HEIGHT,
            frames: int=1,
            path: str = "",
            time_per_frame: float = 0.,
            z_index: int = 1,
            row: int = 1,
            col: int = 1,
            total_cols: int = 1,
            total_rows: int = 1,
            position: tuple[int | float, int | float] | None = None,
       ) -> BaseImage:
        match image_type: 
            case ImageType.FRAME_IMAGE:
                return FrameImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_type=image_type,
                            frames=frames,
                            path=path,
                            time_per_frame=time_per_frame,
                            z_index=z_index,
                            position=position,
                    )
            case ImageType.PIXEL_IMAGE:
                return PixelImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_type=image_type,
                            position=position,
                            z_index=z_index,
                    )
            case ImageType.GRID_IMAGE:
                return GridImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_type=image_type,
                            z_index=z_index,
                            row=row,
                            col=col,
                            total_rows=total_rows,
                            total_cols=total_cols,
                            path=path,
                            position=position,
                    )
            case ImageType.PNG_IMAGE:
                return PngImage(
                            renderer=self.__renderer,
                            width=width,
                            height=height,
                            image_type=image_type,
                            z_index=z_index,
                            path=path,
                            position=position,
                            time_per_frame=time_per_frame,
                    )
