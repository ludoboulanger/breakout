from pygame import Rect, draw, display
from typing import List

from colors import FIREBRICK
from game_area import GameArea
from brick import Brick

class BrickWall:
    def __init__(self, game_area: GameArea) -> None:
        self._rect = Rect(0, 0, 700, 160)
        self._rect.centerx = game_area.rect.centerx
        self._rect.top = game_area.rect.top + 50
        self._bricks: List[Brick] = self._create_bricks()

    @property
    def bricks(self):
        return self._bricks

    def draw_bricks(self):
        surface = display.get_surface()
        for brick in self._bricks:
            draw.rect(surface, brick.color, brick.rect)

    def remove(self, brick: Brick):
        self.bricks.remove(brick)

    def _create_bricks(self) -> List[Brick]:
        bricks = []
        brick_width = 50
        brick_height = 20
        for i in range(8):
            for j in range(14):
                brick = Brick(
                    self._rect.x + j * brick_width,
                    self._rect.y + i * brick_height,
                    brick_width,
                    brick_height,
                    FIREBRICK)
                bricks.append(brick)
        return bricks
