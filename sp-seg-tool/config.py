import os

import toml
from pydantic import BaseModel


class GUIConf(BaseModel):
    width: int
    height: int
    roll_x: int | None = 30
    roll_y: int | None = 30
    base_dir: str
    transparency_factor: int
    scene_width: int
    scene_height: int
    depth_gamma_factor: float | None = 0.5


class ToolbarConf(BaseModel):
    pass


class Conf(BaseModel):
    gui: GUIConf
    toolbar: ToolbarConf

    @staticmethod
    def load_from(path: os.PathLike | str):
        with open(path, "rt") as file:
            load = toml.load(file)
        return Conf(**load)
