from dataclasses import dataclass
from pygame import Rect
from typing import Tuple
from colors import FIREBRICK

@dataclass
class Brick:
    left: int
    top: int
    width: int
    height: int
    color: Tuple[int, int, int]

    def __post_init__(self):
        self.rect = Rect(self.left, self.top, self.width, self.height)