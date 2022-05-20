import pygame
import random

from main import screen


def dice(self):

    self.screen = screen
    color = (170, 170, 170)
    roll_button = pygame.draw.rect(screen, color, pygame.Rect(250, 450, 50, 50))
    small_font = pygame.font.SysFont('Corbel', 35)
    text = small_font.render('Roll', True, (0, 0, 0))
    screen.blit(text, (250, 450))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if roll_button.collidepoint(event.pos):
                    counter = 0
                    while counter < 10:
                        number = random.randint (1, 6)
                        if number == 1:
                            dice_rolled = pygame.image.load('dé_1.jpg')
                            screen.blit(dice_rolled, (300, 450))
                        elif number == 2:
                            dice_rolled = pygame.image.load('dé_2.jpg')
                            screen.blit(dice_rolled, (300, 450))
                        elif number == 3:
                            dice_rolled = pygame.image.load('dé_3.jpg')
                            screen.blit(dice_rolled, (300, 450))
                        elif number == 4:
                            dice_rolled = pygame.image.load('dé_4.jpg')
                            screen.blit(dice_rolled, (300, 450))
                        elif number == 5:
                            dice_rolled = pygame.image.load('dé_5.jpg')
                            screen.blit(dice_rolled, (300, 450))
                        else:
                            dice_rolled = pygame.image.load('dé_6.jpg')
                            screen.blit(dice_rolled, (300, 450))

                        counter = counter + 1

                        if counter == 9:
                            result = number

                    if result == 1:
                            dice_rolled = pygame.image.load('dé_1.jpg')
                            screen.blit(dice_rolled, (300, 450))
                    elif result == 2:
                            dice_rolled = pygame.image.load('dé_2.jpg')
                            screen.blit(dice_rolled, (300, 450))
                    elif result == 3:
                            dice_rolled = pygame.image.load('dé_3.jpg')
                            screen.blit(dice_rolled, (300, 450))
                    elif result == 4:
                            dice_rolled = pygame.image.load('dé_4.jpg')
                            screen.blit(dice_rolled, (300, 450))
                    elif result == 5:
                            dice_rolled = pygame.image.load('dé_5.jpg')
                            screen.blit(dice_rolled, (300, 450))
                    else:
                            dice_rolled = pygame.image.load('dé_6.jpg')
                            screen.blit(dice_rolled, (300, 450))


