from pygame import font
from pygame.font import Font

from colors import WHITE

class Score:

    def __init__(self) -> None:
        font.init()
        self._value = 0
        text_font = Font(None, 48)
        self._text = text_font.render(f"Score : {self._value}", 1, WHITE)
        self._rect = self._text.get_rect()
        self._rect.x = 20
        self._rect.y = 15

    @property
    def image(self):
        return self._text

    @property
    def rect(self):
        return self._rect

    def update(self):
        text_font = Font(None, 48)
        self._text = text_font.render(f"Score : {self._value}", 1, WHITE)

    def increment(self):
        self._value += 1

    def reset(self):
        self._value = 0