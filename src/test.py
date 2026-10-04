import json
import tkinter as tk
from pathlib import Path

from PIL import Image, ImageTk


ATLAS_PATH = Path("src/assests/alpha/alpha.png")
METADATA_PATH = Path("src/test.json")


class BitmapFont:
    def __init__(
        self,
        atlas_path: Path,
        metadata_path: Path,
    ) -> None:
        with metadata_path.open("r", encoding="utf-8") as file:
            self.metadata = json.load(file)

        self.image = Image.open(atlas_path).convert("RGBA")

        atlas = self.metadata["atlas"]

        self.origin_x, self.origin_y = atlas["origin"]

        cell = atlas["cell"]
        self.char_width = cell["width"]
        self.char_height = cell["height"]

        stride = atlas["stride"]
        self.stride_x = stride["x"]
        self.stride_y = stride["y"]

        self.columns = atlas["columns"]
        self.character_count = atlas["characters"]

        self.first_character = atlas.get("first_character", 32)

        self.glyphs: dict[str, Image.Image] = {}

        self._load_glyphs()

    def _load_glyphs(self) -> None:
        """Extract every character from the bitmap font atlas."""

        for index in range(self.character_count):
            char_code = self.first_character + index

            row = index // self.columns
            column = index % self.columns

            x = self.origin_x + column * self.stride_x
            y = self.origin_y + row * self.stride_y

            glyph = self.image.crop(
                (
                    x,
                    y,
                    x + self.char_width,
                    y + self.char_height,
                )
            )

            self.glyphs[chr(char_code)] = glyph

    def render(
        self,
        text: str,
        scale: int = 1,
    ) -> Image.Image:
        """Render text using the bitmap font."""

        if not text:
            return Image.new(
                "RGBA",
                (1, self.char_height * scale),
                (0, 0, 0, 0),
            )

        width = len(text) * self.stride_x
        height = self.char_height

        result = Image.new(
            "RGBA",
            (width, height),
            (0, 0, 0, 0),
        )

        x = 0

        for char in text:
            glyph = self.glyphs.get(char)

            if glyph is None:
                x += self.stride_x
                continue

            result.alpha_composite(glyph, (x, 0))

            x += self.stride_x

        if scale != 1:
            result = result.resize(
                (
                    result.width * scale,
                    result.height * scale,
                ),
                Image.Resampling.NEAREST,
            )

        return result


class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Bitmap Font")

        self.font = BitmapFont(
            ATLAS_PATH,
            METADATA_PATH,
        )

        self.canvas = tk.Canvas(
            self.root,
            width=1000,
            height=300,
            bg="white",
        )

        self.canvas.pack()

        self.draw_text(
            "HELLO PACMAN!",
            x=20,
            y=20,
            scale=2,
        )

        self.root.mainloop()

    def draw_text(
        self,
        text: str,
        x: int,
        y: int,
        scale: int = 1,
    ) -> None:
        image = self.font.render(
            text,
            scale,
        )

        self.tk_image = ImageTk.PhotoImage(image)

        self.canvas.create_image(
            x,
            y,
            image=self.tk_image,
            anchor="nw",
        )


if __name__ == "__main__":
    App()
