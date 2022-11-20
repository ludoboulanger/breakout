from pygame import display, Surface
import numpy as np

from colors import WHITE
from game_area import GameArea
from plateform import Plateform


class Ball:

    def __init__(self, plateform: Plateform, game_area: GameArea) -> None:
        screen = display.get_surface()
        self._plateform = plateform
        self._game_area = game_area
        self._image = Surface([10, 10])
        self._image.fill(WHITE)
        self._rect = self._image.get_rect()
        self._rect.x = screen.get_width() //2
        self._rect.y = int(2 * screen.get_height() / 3)

        start_x_velocity = np.random.choice([-3, 3])
        self._velocities = [start_x_velocity, 3]

    @property
    def image(self):
        return self._image

    @property
    def rect(self):
        return self._rect

    def update(self):
        self._calculate_new_vector()
        self._rect = self._rect.move(self._velocities)

    def _calculate_new_vector(self):
        if self._hit_wall_left() or self._hit_wall_right():
            self._velocities[0] *= -1
        elif self._hit_top():
            self._velocities[1] *= -1
        elif self._hit_plateform_left():
            self._velocities[1] *= -1
            if not self._is_going_left():
                self._velocities[0] *= -1
        elif self._hit_plateform_right():
            self._velocities[1] *= -1
            if self._is_going_left():
                self._velocities[0] *= -1

    def _hit_wall_right(self):
        return self._rect.colliderect(self._game_area.wall_right)

    def _hit_wall_left(self):
        return self._rect.colliderect(self._game_area.wall_left)

    def _hit_top(self):
        return self._rect.colliderect(self._game_area.wall_top)

    def _miss(self):
        return self._rect.y > self._plateform.rect.centery

    def _hit_plateform_left(self):
        return self._rect.colliderect(self._plateform.rect) \
            and self._rect.x < self._plateform.rect.centerx

    def _hit_plateform_right(self):
        return self._rect.colliderect(self._plateform.rect) \
            and self._rect.x >= self._plateform.rect.centerx

    def _is_going_left(self):
        return self._velocities[0] < 0

    def _normalize_angle(self, angle):
        if angle > np.pi and angle < 2*np.pi:
            return -angle
        return angle