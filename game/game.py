import sys
from pygame import init, font, display, Surface, time
from pygame import key, event, QUIT, K_RIGHT, K_LEFT

from colors import BLACK
from ball import Ball
from brick_wall import BrickWall
from game_area import GameArea
from score import Score
from plateform import Plateform


class Game:
    def __init__(self) -> None:
        init()
        font.init()
        display.set_caption("Breakout")

        self._screen = display.set_mode(size=(800, 800))

        self._background = Surface(self._screen.get_size())
        self._background = self._background.convert()
        self._background.fill(BLACK)

        self._game_area = GameArea()
        self._brick_wall = BrickWall(self._game_area)
        self._plateform = Plateform(self._game_area)
        self._ball = Ball()
        self._score = Score()

        self._screen.blit(self._background, (0, 0))
        display.update()

    def play(self):
        clock = time.Clock()
        game_is_in_progress = True
        while game_is_in_progress:
            clock.tick(60)
            self._handle_ball_collisions()
            self._handle_events()
            self._update_screen()
            game_is_in_progress = self.check_game_status()

    def _update_screen(self):
        self._ball.update()
        self._score.update()
        self._screen.blit(self._background, (0, 0))
        self._game_area.draw_borders()
        self._brick_wall.draw_bricks()
        self._screen.blit(self._score.image, self._score.rect)
        self._screen.blit(self._plateform.image, self._plateform.rect)
        self._screen.blit(self._ball.image, self._ball.rect)
        display.flip()

    def _handle_ball_collisions(self):
        ball_rect = self._ball.rect
        if ball_rect.colliderect(self._game_area.wall_right):
            self._ball.handle_collision_wall_right()
        elif ball_rect.colliderect(self._game_area.wall_left):
            self._ball.handle_collision_wall_left()
        elif ball_rect.colliderect(self._game_area.wall_top):
            self._ball.handle_collision_wall_top()
        elif ball_rect.colliderect(self._plateform.rect)\
            and ball_rect.x < self._plateform.rect.centerx:
            self._ball.handle_collision_plateform_left()
        elif ball_rect.colliderect(self._plateform.rect)\
            and ball_rect.x >= self._plateform.rect.centerx:
            self._ball.handle_collision_plateform_right()
    
    def _handle_events(self):
        for e in event.get():  
            if e.type == QUIT:
                sys.exit()
            
        key_input = key.get_pressed()
        if key_input[K_RIGHT]:
            self._plateform.move_right()
        if key_input[K_LEFT]:
            self._plateform.move_left()

        self._handle_brick_collisions()

    def _handle_brick_collisions(self):
        active_bricks = self._brick_wall.bricks
        for brick in active_bricks:
            if self._ball.rect.colliderect(brick.rect):
                self._ball.handle_brick_collision(brick)
                self._brick_wall.remove(brick)
                self._score.increment()

    def check_game_status(self):
        return self._ball.rect.y < self._plateform.rect.bottom

if __name__ == "__main__":
    game = Game()
    game.play()