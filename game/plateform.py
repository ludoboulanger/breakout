from pygame import Surface, display

from game_area import GameArea
from colors import WHITE


class Plateform():
    def __init__(self, game_area: GameArea) -> None:
        self._game_area = game_area
        self._image = Surface([80, 10])
        self._image.fill(WHITE)
        self._rect = self._image.get_rect()

        screen = display.get_surface()
        self._dx = 10
        start_pos = [screen.get_width() // 2, game_area.rect.bottom - 30]
        self._rect.centerx, self._rect.centery = start_pos

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    def move_right(self):
        if not self._rect.colliderect(self._game_area.wall_right):
            self._rect = self.rect.move([self._dx, 0])

    def move_left(self):
        if not self._rect.colliderect(self._game_area.wall_left):
            self._rect = self.rect.move([-self._dx, 0])