import os
from pydantic import BaseModel, model_validator, Field


class Config(BaseModel):
    highscore_filename: str = Field(default="path_to_highscore_filename")
    levels: list[int] = Field(
        default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], max_length=10
    )
    width: list[int] = Field(default_factory=lambda: [30] * 10, max_length=10)
    height: list[int] = Field(default_factory=lambda: [30] * 10, max_length=10)
    lives: int = Field(default=3, gt=0, lt=10)
    pacgum: int = Field(default=10, gt=20)
    points_per_pacgum: int = Field(default=20, ge=10, le=40)
    points_per_super_pacgum: int = Field(default=30, ge=20, le=60)
    points_per_ghost: int = Field(default=30, ge=20, le=60)
    seed: int = Field(default=10)
    level_max_time: int = Field(default=200, ge=100, le=300)

    def validate_level(self, level: int, index: int) -> None:
        if level < 1 or level >= 20:
            raise ValueError(
                f"Invalid level: {level} in index {index}."
                "Each level must be between 1 and 20 (inclusive)."
            )

    def validate_width(self, width: int, index: int) -> None:
        if width < 10 or width >= 100:
            raise ValueError(
                f"Invalid width: {width} in index {idx}."
                "Width must be between 10 and 100 (inclusive)."
            )

    def validate_height(self, height: int, index: int) -> None:
        if height < 10 or height >= 100:
            raise ValueError(
                f"Invalid height: {height} in index {idx}"
                "Height must be between 10 and 100 (inclusive)."
            )

    @model_validator(mode='after')
    def validate_highscore_filename(self) -> Self:
        if not os.path.exists(self.highscore_filename):
            raise ValueError(f"Error: {self.highscore_filename} doesn't exists!")
        elif not os.access(self.highscore_filename, os.R_OK):
            raise ValueError(
                f"Error: {self.highscore_filename} permission denied!."
            )
        return self

    @model_validator(mode='after')
    def validate_level_dimension(self) -> Self:
        set_levels = set(self.levels)
        if len(set_levels) == len(self.width) == len(self.height):
            idx = 0
            for level, width, height in zip(self.levels, self.width, self.height):
                self.validate_level(level, idx)
                self.validate_width(width, idx)
                self.validate_height(height, idx)
                idx += 1
        else:
            raise ValueError(
                "Invalid configuration: 'levels', 'width', and 'height' "
                "must contain the same number of elements."
            )
        return self

