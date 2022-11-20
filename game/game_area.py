from pygame import display, Surface, draw, Rect

from colors import WHITE

class GameArea:

    def __init__(self) -> None:
        screen = display.get_surface()
        width = 0.9 * screen.get_width()
        height = 0.9 * screen.get_height()

        self._image = Surface([width, height])
        self._rect = self._image.get_rect()
        self._rect.centerx = screen.get_width() // 2
        self._rect.y = 60

        border_width = 10
        self._wall_right = Rect(self._rect.right - border_width, self._rect.y, border_width, self._rect.height)
        self._wall_left = Rect(self._rect.x, self._rect.y, border_width, self._rect.height)
        self._wall_top = Rect(self._rect.x, self._rect.y, self._rect.width, border_width)
        self._wall_bottom = Rect(self._rect.x, self._rect.bottom - border_width, self._rect.width, border_width)

    @property
    def rect(self):
        return self._rect

    @property
    def image(self):
        return self._image

    @property
    def position(self):
        return 50, 50

    @property
    def wall_right(self):
        return self._wall_right

    @property
    def wall_left(self):
        return self._wall_left

    @property
    def wall_bottom(self):
        return self._wall_bottom

    @property
    def wall_top(self):
        return self._wall_top

    def draw_borders(self,):
        surface = display.get_surface()
        draw.rect(surface, WHITE, self._wall_right)
        draw.rect(surface, WHITE, self._wall_left)
        draw.rect(surface, WHITE, self._wall_top)
        draw.rect(surface, WHITE, self._wall_bottom)