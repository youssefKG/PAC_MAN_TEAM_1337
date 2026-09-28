
from src.mlx.libmlx import mlx, mlx_image_t, mlx_loop_hook_func
import ctypes
import random

class MLX:
    def __init__(self) -> None:
        self.__mlx_ptr: ctypes.c_void_p = mlx.mlx_init(1700, 1700, b"MLX hello world")
        self.__image: mlx_image_t = mlx.mlx_new_image(self.__mlx_ptr, 200, 200)


    def ft_pixel(self, r: int, g: int, b: int, a: int) -> int:
        """ Packs RGBA values into a single 32-bit integer. """
        return (r << 24) | (g << 16) | (b << 8) | a

    @mlx_loop_hook_func
    def ft_randomize():
        for i in range(self.__image.contents.width):
            for y in range(self.__image.contents.height):
                color = self.ft_pixel(
                    random.randint(0, 255),  # R
                    random.randint(0, 255),  # G
                    random.randint(0, 255),  # B
                    random.randint(0, 255)   # A
                )
                mlx.mlx_put_pixel(image, i, y, color)


