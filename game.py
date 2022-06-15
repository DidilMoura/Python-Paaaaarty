import pygame
import random

def game():

    #définition fenêtre de jeu
    pygame.display.set_caption("Python Parthy")
    screen_game = pygame.display.set_mode((600,  600))
    background_game = pygame.image.load('plateau_python_party.png')
    background_game = pygame.transform.scale(background_game, (600, 600))
    screen_game.blit(background_game, (0, 0))
    pygame.display.flip()

    #Variable
    player_1_pos = 0
    player_2_pos = 0
    score = 0

    def roll_dice(x):
        color = (170, 170, 170)
        roll_button = pygame.draw.rect(screen_game, color, pygame.Rect(250, 400, 50, 30))
        small_font = pygame.font.SysFont('Corbel', 35)
        text = small_font.render('Roll', True, (0, 0, 0))
        screen_game.blit(text, (250, 400))
        pygame.display.flip()

        boucle = True

        while boucle:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    boucle = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if roll_button.collidepoint(event.pos):
                        counter = 0
                        while counter < 10:
                            number = random.randint(1, 6)
                            if number == 1:
                                dice_rolled = pygame.image.load('dé_1.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            elif number == 2:
                                dice_rolled = pygame.image.load('dé_2.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            elif number == 3:
                                dice_rolled = pygame.image.load('dé_3.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            elif number == 4:
                                dice_rolled = pygame.image.load('dé_4.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            elif number == 5:
                                dice_rolled = pygame.image.load('dé_5.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            else:
                                dice_rolled = pygame.image.load('dé_6.jpg')
                                screen_game.blit(dice_rolled, (300, 375))
                            counter = counter + 1
                            pygame.display.flip()

                        if number == 1:
                            dice_rolled = pygame.image.load('dé_1.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        elif number == 2:
                            dice_rolled = pygame.image.load('dé_2.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        elif number == 3:
                            dice_rolled = pygame.image.load('dé_3.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        elif number == 4:
                            dice_rolled = pygame.image.load('dé_4.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        elif number == 5:
                            dice_rolled = pygame.image.load('dé_5.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        else:
                            dice_rolled = pygame.image.load('dé_6.jpg')
                            screen_game.blit(dice_rolled, (300, 375))
                        pygame.display.flip()
                        boucle = False
        x = number
        return x


    while player_1_pos <= 25 and player_2_pos <= 25:
        result = roll_dice(score)
        player_1_pos = player_1_pos + result


    if player_1_pos > 25:
        font = pygame.font.SysFont('Corbel', 35)
        victory_text = font.render('Player 1 won', True, (0, 0, 0))
        screen_game.blit(victory_text, (200, 350))
        pygame.display.flip()

    boucle = True

    while boucle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                test = False
                pygame.quit()
