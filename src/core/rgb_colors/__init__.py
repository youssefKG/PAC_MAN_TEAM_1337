from enum import Enum


def create_color(r: int, g: int, b: int, t: int=0xFF000000) -> int:
    """Create a 32-bit ARGB color value from RGB components."""
    return t << 24 | (r << 16) | (g << 8) | b


class RgbColors(Enum):
    BLACK          = 0xFF000000
    WHITE          = 0xFFFFFFFF
    RED            = 0xFFFF0000
    GREEN          = 0xFF00FF00
    BLUE           = 0xFF0000FF

    YELLOW         = 0xFFFFFF00
    CYAN           = 0xFF00FFFF
    MAGENTA        = 0xFFFF00FF

    GRAY           = 0xFF808080
    DARK_GRAY      = 0xFF404040
    LIGHT_GRAY     = 0xFFC0C0C0

    ORANGE         = 0xFFFFA500
    PURPLE         = 0xFF800080
    PINK           = 0xFFFFC0CB
    BROWN          = 0xFFA52A2A

    NAVY           = 0xFF000080
    TEAL           = 0xFF008080
    LIME           = 0xFF00FF00
    OLIVE          = 0xFF808000
    MAROON         = 0xFF800000
    SILVER         = 0xFFC0C0C0
    BLACK_TRANS    = 0x0F000001

__all__ = ["RgbColors"]
