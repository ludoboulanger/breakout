from pygame import display, Surface
import numpy as np

from brick import Brick
from colors import WHITE


class Ball:

    def __init__(self) -> None:
        screen = display.get_surface()
        self._image = Surface([10, 10])
        self._image.fill(WHITE)
        self._rect = self._image.get_rect()
        self._rect.x = screen.get_width() //2
        self._rect.y = int(2 * screen.get_height() / 3)

        start_x_velocity = np.random.choice([-4, 4])
        self._velocities = [start_x_velocity, -4]

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    def update(self):
        self._rect = self._rect.move(self._velocities)

    def handle_collision_wall_right(self):
        self._velocities[0] *= -1
    
    def handle_collision_wall_left(self):
        self._velocities[0] *= -1

    def handle_collision_wall_top(self):
        self._velocities[1] *= -1

    def handle_collision_plateform_right(self):
        self._velocities[1] *= -1
        if self._is_going_left():
            self._velocities[0] *= -1

    def handle_collision_plateform_left(self):
        self._velocities[1] *= -1
        if not self._is_going_left():
            self._velocities[0] *= -1

    def handle_brick_collision(self, brick: Brick):
        if self._hit_left(brick) or self._hit_right(brick):
            self._velocities[0] *= -1
        elif self._hit_top(brick) or self._hit_bottom(brick):
            self._velocities[1] *= -1
    
    def _is_going_left(self):
        return self._velocities[0] < 0

    def _hit_bottom(self, brick: Brick):
        return brick.rect.collidepoint(self._rect.centerx, self._rect.bottom)

    def _hit_top(self, brick: Brick):
        return brick.rect.collidepoint(self._rect.centerx, self._rect.top)

    def _hit_left(self, brick: Brick):
        return brick.rect.collidepoint(self._rect.left, self._rect.centery)

    def _hit_right(self, brick: Brick):
        return brick.rect.collidepoint(self._rect.right, self._rect.centery)
