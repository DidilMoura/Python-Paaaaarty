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
    pion_1 = pygame.image.load('caracteres_1.png')
    pion_1 = pygame.transform.scale(pion_1, (40, 40))
    pion_2 = pygame.image.load('caracteres_2.png')
    pion_2 = pygame.transform.scale(pion_2, (40, 40))

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

    def player_1_before_movements(x):
        screen_game.blit(background_game, (0, 0))
        if x == 0:
            screen_game.blit(pion_2, (60, 128))
        elif x == 1:
            screen_game.blit(pion_2, (190, 128))
        elif x == 2:
            screen_game.blit(pion_2, (250, 128))
        elif x == 3:
            screen_game.blit(pion_2, (310, 128))
        elif x == 4:
            screen_game.blit(pion_2, (370, 128))
        elif x == 5:
            screen_game.blit(pion_2, (430, 128))
        elif x == 6:
            screen_game.blit(pion_2, (460, 160))
        elif x == 7:
            screen_game.blit(pion_2, (460, 220))
        elif x == 8:
            screen_game.blit(pion_2, (430, 245))
        elif x == 8:
            screen_game.blit(pion_2, (430, 245))
        elif x == 9:
            screen_game.blit(pion_2, (370, 245))
        elif x == 10:
            screen_game.blit(pion_2, (310, 245))
        elif x == 11:
            screen_game.blit(pion_2, (250, 245))
        elif x == 12:
            screen_game.blit(pion_2, (190, 245))
        elif x == 13:
            screen_game.blit(pion_2, (130, 245))
        elif x == 14:
            screen_game.blit(pion_2, (70, 245))
        elif x == 15:
            screen_game.blit(pion_2, (70, 305))
        elif x == 16:
            screen_game.blit(pion_2, (70, 365))
        elif x == 17:
            screen_game.blit(pion_2, (70, 425))
        elif x == 18:
            screen_game.blit(pion_2, (70, 485))
        elif x == 19:
            screen_game.blit(pion_2, (130, 485))
        elif x == 20:
            screen_game.blit(pion_2, (190, 485))
        elif x == 21:
            screen_game.blit(pion_2, (250, 515))
        elif x == 22:
            screen_game.blit(pion_2, (310, 515))
        elif x == 23:
            screen_game.blit(pion_2, (370, 515))
        elif x == 24:
            screen_game.blit(pion_2, (430, 515))
        elif x == 25:
            screen_game.blit(pion_2, (490, 515))
        elif x > 25:
            screen_game.blit(pion_2, (505, 485))

    def player_1_location(x):
        if x == 0:
            screen_game.blit(pion_1, (60, 128))
        elif x == 1:
            screen_game.blit(pion_1, (190, 128))
        elif x == 2:
            screen_game.blit(pion_1, (250, 128))
        elif x == 3:
            screen_game.blit(pion_1, (310, 128))
        elif x == 4:
            screen_game.blit(pion_1, (370, 128))
        elif x == 5:
            screen_game.blit(pion_1, (430, 128))
        elif x == 6:
            screen_game.blit(pion_1, (460, 160))
        elif x == 7:
            screen_game.blit(pion_1, (460, 220))
        elif x == 8:
            screen_game.blit(pion_1, (430, 245))
        elif x == 8:
            screen_game.blit(pion_1, (430, 245))
        elif x == 9:
            screen_game.blit(pion_1, (370, 245))
        elif x == 10:
            screen_game.blit(pion_1, (310, 245))
        elif x == 11:
            screen_game.blit(pion_1, (250, 245))
        elif x == 12:
            screen_game.blit(pion_1, (190, 245))
        elif x == 13:
            screen_game.blit(pion_1, (130, 245))
        elif x == 14:
            screen_game.blit(pion_1, (70, 245))
        elif x == 15:
            screen_game.blit(pion_1, (70, 305))
        elif x == 16:
            screen_game.blit(pion_1, (70, 365))
        elif x == 17:
            screen_game.blit(pion_1, (70, 425))
        elif x == 18:
            screen_game.blit(pion_1, (70, 485))
        elif x == 19:
            screen_game.blit(pion_1, (130, 485))
        elif x == 20:
            screen_game.blit(pion_1, (190, 485))
        elif x == 21:
            screen_game.blit(pion_1, (250, 515))
        elif x == 22:
            screen_game.blit(pion_1, (310, 515))
        elif x == 23:
            screen_game.blit(pion_1, (370, 515))
        elif x == 24:
            screen_game.blit(pion_1, (430, 515))
        elif x == 25:
            screen_game.blit(pion_1, (490, 515))
        elif x > 25:
            screen_game.blit(pion_1, (505, 485))

    def player_2_location(x):
        if x == 0:
            screen_game.blit(pion_2, (60, 128))
        elif x == 1:
            screen_game.blit(pion_2, (190, 128))
        elif x == 2:
            screen_game.blit(pion_2, (250, 128))
        elif x == 3:
            screen_game.blit(pion_2, (310, 128))
        elif x == 4:
            screen_game.blit(pion_2, (370, 128))
        elif x == 5:
            screen_game.blit(pion_2, (430, 128))
        elif x == 6:
            screen_game.blit(pion_2, (460, 160))
        elif x == 7:
            screen_game.blit(pion_2, (460, 220))
        elif x == 8:
            screen_game.blit(pion_2, (430, 245))
        elif x == 8:
            screen_game.blit(pion_2, (430, 245))
        elif x == 9:
            screen_game.blit(pion_2, (370, 245))
        elif x == 10:
            screen_game.blit(pion_2, (310, 245))
        elif x == 11:
            screen_game.blit(pion_2, (250, 245))
        elif x == 12:
            screen_game.blit(pion_2, (190, 245))
        elif x == 13:
            screen_game.blit(pion_2, (130, 245))
        elif x == 14:
            screen_game.blit(pion_2, (70, 245))
        elif x == 15:
            screen_game.blit(pion_2, (70, 305))
        elif x == 16:
            screen_game.blit(pion_2, (70, 365))
        elif x == 17:
            screen_game.blit(pion_2, (70, 425))
        elif x == 18:
            screen_game.blit(pion_2, (70, 485))
        elif x == 19:
            screen_game.blit(pion_2, (130, 485))
        elif x == 20:
            screen_game.blit(pion_2, (190, 485))
        elif x == 21:
            screen_game.blit(pion_2, (250, 515))
        elif x == 22:
            screen_game.blit(pion_2, (310, 515))
        elif x == 23:
            screen_game.blit(pion_2, (370, 515))
        elif x == 24:
            screen_game.blit(pion_2, (430, 515))
        elif x == 25:
            screen_game.blit(pion_2, (490, 515))
        elif x > 25:
            screen_game.blit(pion_2, (505, 485))

    def player_2_before_movements(x):
        screen_game.blit(background_game, (0, 0))
        if x == 0:
            screen_game.blit(pion_1, (60, 128))
        elif x == 1:
            screen_game.blit(pion_1, (190, 128))
        elif x == 2:
            screen_game.blit(pion_1, (250, 128))
        elif x == 3:
            screen_game.blit(pion_1, (310, 128))
        elif x == 4:
            screen_game.blit(pion_1, (370, 128))
        elif x == 5:
            screen_game.blit(pion_1, (430, 128))
        elif x == 6:
            screen_game.blit(pion_1, (460, 160))
        elif x == 7:
            screen_game.blit(pion_1, (460, 220))
        elif x == 8:
            screen_game.blit(pion_1, (430, 245))
        elif x == 8:
            screen_game.blit(pion_1, (430, 245))
        elif x == 9:
            screen_game.blit(pion_1, (370, 245))
        elif x == 10:
            screen_game.blit(pion_1, (310, 245))
        elif x == 11:
            screen_game.blit(pion_1, (250, 245))
        elif x == 12:
            screen_game.blit(pion_1, (190, 245))
        elif x == 13:
            screen_game.blit(pion_1, (130, 245))
        elif x == 14:
            screen_game.blit(pion_1, (70, 245))
        elif x == 15:
            screen_game.blit(pion_1, (70, 305))
        elif x == 16:
            screen_game.blit(pion_1, (70, 365))
        elif x == 17:
            screen_game.blit(pion_1, (70, 425))
        elif x == 18:
            screen_game.blit(pion_1, (70, 485))
        elif x == 19:
            screen_game.blit(pion_1, (130, 485))
        elif x == 20:
            screen_game.blit(pion_1, (190, 485))
        elif x == 21:
            screen_game.blit(pion_1, (250, 515))
        elif x == 22:
            screen_game.blit(pion_1, (310, 515))
        elif x == 23:
            screen_game.blit(pion_1, (370, 515))
        elif x == 24:
            screen_game.blit(pion_1, (430, 515))
        elif x == 25:
            screen_game.blit(pion_1, (490, 515))
        elif x > 25:
            screen_game.blit(pion_1, (505, 485))


    while player_1_pos <= 26 and player_2_pos <= 26:
        #initialise les positions de départs des pions
        player_1_location(player_1_pos)
        player_2_location(player_2_pos)

        #lancé de dé et déplacement du joueur 1
        result = roll_dice(score)
        player_1_pos = player_1_pos + result
        player_1_before_movements(player_2_pos)
        player_1_location(player_1_pos)

        #lancé de dé et déplacement du joueur 2
        result = roll_dice(score)
        player_2_pos = player_2_pos + result
        player_2_before_movements(player_1_pos)
        player_2_location(player_2_pos)


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
