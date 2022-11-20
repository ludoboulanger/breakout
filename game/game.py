import sys
from pygame import init, font, display, Surface, time
from pygame import key, event, QUIT, K_RIGHT, K_LEFT

from colors import BLACK
from ball import Ball
from game_area import GameArea
from score import Score
from plateform import Plateform


class Game:

    def __init__(self) -> None:
        init()
        font.init()
        display.set_caption("Breakout")

        self.screen = display.set_mode(size=(800, 800))

        self.background = Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(BLACK)

        self.game_area = GameArea()
        self.plateform = Plateform(self.game_area)
        self.ball = Ball(self.plateform, self.game_area)
        self.score = Score()

        self.screen.blit(self.background, (0, 0))
        display.update()


    def play(self):
        clock = time.Clock()
        while True:
            clock.tick(60)
            self.handle_events()
            self.update_screen()

    def update_screen(self):
        self.ball.update()
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.game_area.image, self.game_area.position)
        self.screen.blit(self.score.image, self.score.rect)
        self.screen.blit(self.plateform.image, self.plateform.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
        self.game_area.draw_borders()
        display.flip()

    def handle_events(self):
        for e in event.get():  
            if e.type == QUIT:
                sys.exit()
            
        key_input = key.get_pressed()
        if key_input[K_RIGHT]:
            self.plateform.move_right()
        if key_input[K_LEFT]:
            self.plateform.move_left()



if __name__ == "__main__":
    game = Game()
    game.play()