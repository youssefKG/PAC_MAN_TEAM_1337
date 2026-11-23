from src.core import Engine, FrameImage, ImageType, PixelImage, PngImage

class Entity:
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        col: int,
        row: int,
        cell_size: int,
        cell_border_size: int,
        cell_content_size: int
    ) -> None:
        self._engine: Engine = engine
        self._parent: PixelImage | PngImage = parent
        self._col: int = col
        self._row: int = row
        self._cell_size: int = cell_size
        self._cell_border_size: int = cell_border_size
        self._cell_content_size: int = cell_content_size
        self._position: tuple[int, int] = (
            col * self._cell_size + self._cell_border_size,
            self._row * self._cell_size + self._cell_border_size
        )

class Pacman(Entity): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        col: int,
        row: int,
        cell_size: int,
        cell_border_size: int,
        cell_content_size: int
    ) -> None:
        super().__init__(
            engine=engine,
            parent=parent,
            col=col,
            row=row,
            cell_size=cell_size,
            cell_border_size=cell_border_size,
            cell_content_size=cell_content_size
        )
        self._pacman: FrameImage = self.__new_pacman()


    def __new_pacman(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=self._cell_content_size,
            height=self._cell_content_size,
            path="src/assests/frames/pacman.png",
            time_per_frame=.2,
            position=self._position,
            frames=8,
        ).set_parent(self._parent).to_center().create()


class OrangeGhost(Entity): 
    def __init__(
        self,
        /,
        *,
        engine: Engine,
        parent: PixelImage | PngImage,
        col: int,
        row: int,
        cell_size: int,
        cell_border_size: int,
        cell_content_size: int
    ) -> None:
        super().__init__(
            engine=engine,
            parent=parent,
            col=col,
            row=row,
            cell_size=cell_size,
            cell_border_size=cell_border_size,
            cell_content_size=cell_content_size
        )
        self.__orange_ghost: FrameImage = self.__new_orange_ghost()


    def __new_orange_ghost(self) -> FrameImage:
        return self._engine.new_image(
            image_type=ImageType.FRAME_IMAGE,
            width=self._cell_content_size,
            height=self._cell_content_size,
            path="src/assests/frames/pacman.png",
            time_per_frame=.2,
            position=self._position,
            frames=8,
        ).set_parent(self._parent).to_center().create()
