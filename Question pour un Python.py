import pygame
import sys

# --- Colors --- #
white = (255, 255, 255)
light_gray = (170, 170, 170)
dark_gray = (100, 100, 100)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Question pour un Python')
        self.in_game = True

    def game_loop(self):
        while self.in_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.in_game = False
            pygame.display.update()


game = Game()
game.game_loop()


