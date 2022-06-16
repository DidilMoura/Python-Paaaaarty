import pygame
import random
import json

pygame.init()


def coin_flip_game():
    """
Function of the game coin flip
    :return: nothing
    """

    # open the folder with player location loaded in to change them after the game
    try:
        with open('players_pos.txt') as score_file:
            data = json.load(score_file)
    except:
        print('No file created yet')

    # loading the screen
    screen = pygame.display.set_mode((600,  600))
    screen.fill((255, 255, 255))
    small_font = pygame.font.SysFont('Corbel', 35)
    heads_button = pygame.draw.rect(screen, (240, 80, 54), pygame.Rect(100, 150, 100, 50))
    heads_name = small_font.render('Heads', True, (0, 0, 0))
    screen.blit(heads_name, (108, 150))
    tails_button = pygame.draw.rect(screen, (0, 123, 194), pygame.Rect(400, 150, 100, 50))
    heads_name = small_font.render('Tails', True, (0, 0, 0))
    screen.blit(heads_name, (412, 150))
    pygame.display.flip()

    heads_coin = pygame.image.load('piece_pile.png')
    heads_coin = pygame.transform.scale(heads_coin, (50, 50))
    tails_coin = pygame.image.load('piece_face.png')
    tails_coin = pygame.transform.scale(tails_coin, (50, 50))

    value = 0

    # select the order of play for the players
    order_select = random.randint(1, 2)
    if order_select == 1:  # if it's 1 the player 1 is the first player
        text = small_font.render('Player 1 chose', True, (0, 0, 0))
        screen.blit(text, (200, 50))
        first_player = data['player_1_pos']  # player choosing heads or tails
        second_player = data['player_2_pos']
    elif order_select == 2:  # if it's 2 the player 2 is the first
        text = small_font.render('Player 2 chose', True, (0, 0, 0))
        screen.blit(text, (200, 50))
        first_player = data['player_2_pos']
        second_player = data['player_1_pos']

    heads_button = pygame.draw.rect(screen, (240, 80, 54), pygame.Rect(100, 150, 100, 50))
    heads_name = small_font.render('Heads', True, (0, 0, 0))
    screen.blit(heads_name, (108, 150))

    tails_button = pygame.draw.rect(screen, (0, 123, 194), pygame.Rect(400, 150, 100, 50))
    heads_name = small_font.render('Tails', True, (0, 0, 0))
    screen.blit(heads_name, (412, 150))

    pygame.display.flip()

    def coin_flip_animation():
        """
Animation of the coin flip
        :return: the value of the coin fliping
        """
        length = 300
        width = 500
        for i in range(16):  # loop to animate the coin
            while i < 9:  # coin moving to the top during this loop
                screen.fill((255, 255, 255))
                screen.blit(heads_coin, (length, width))
                pygame.display.flip()
                width -= 70
                screen.fill((255, 255, 255))
                screen.blit(tails_coin, (length, width))
                pygame.display.flip()
                width -= 70
                i += 1

            while 9 <= i < 16:  # coin moving to the bot during this loop
                screen.fill((255, 255, 255))
                screen.blit(heads_coin, (length, width))
                pygame.display.flip()
                width += 70
                screen.fill((255, 255, 255))
                screen.blit(tails_coin, (length, width))
                pygame.display.flip()
                width += 70
                i += 1
                pygame.display.flip()
        result = random.randint(0, 1)

        # show the result of the coin flip
        if result == 0:
            screen.fill((255, 255, 255))
            screen.blit(heads_coin, (300, 500))
            pygame.time.wait(3000)
            pygame.display.flip()
        elif result == 1:
            screen.fill((255, 255, 255))
            screen.blit(tails_coin, (300, 500))
            pygame.display.flip()
        return result  # return the value of the result

    running = True

    # infinite loop
    while running:

        # detect on which button the player click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heads_button.collidepoint(event.pos):
                    score = coin_flip_animation()  # call the function and attribute the result to score variable
                    """If the score is 1 the first player lose so we search who is the first player to allocate the 
                    malus of the player location variable"""
                    if score == 1:
                        malus = random.randint(1, 3)
                        if first_player == data['player_1_pos']:
                            data['player_1_pos'] -= malus
                        elif first_player == data['player_2_pos']:
                            data['player_2_pos'] -= malus
                    elif score == 0:  # if the score is 0 we look for the second player to attribute the malus
                        malus = random.randint(1, 3)
                        if second_player == data['player_1_pos']:
                            data['player_1_pos'] -= malus
                        elif second_player == data['player_2_pos']:
                            data['player_2_pos'] -= malus
                    with open('players_pos', 'w') as score_file:  # save the change in the file, and we close the game
                        json.dump(data, score_file)
                    pygame.display.quit()
                elif tails_button.collidepoint(event.pos):
                    score = coin_flip_animation()
                    if score == 1:
                        malus = random.randint(1, 3)
                        if second_player == data['player_2_pos']:
                            data['player_2_pos'] -= malus
                        elif second_player == data['player_1_pos'] :
                            data['player_1_pos'] -= malus
                    elif score == 0:
                        malus = random.randint(1, 3)
                        if first_player == data['player_2_pos']:
                            data['player_2_pos'] -= malus
                        elif first_player == data['player_1_pos']:
                            data['player_1_pos'] -= malus
                    with open('players_pos', 'w') as score_file:
                        json.dump(data, score_file)
                    pygame.display.quit()
            if event.type == pygame.QUIT:
                pygame.quit()


