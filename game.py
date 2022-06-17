import pygame
import random
import json
from clicker_duel import clicker_game
from coin_flip import coin_flip_game


def game():
    """
Principal function of the project. It launches the game, manage player turn and location, launches the other game and
manage the game board with player movements.
    :return: nothing
    """
    # game window
    pygame.display.set_caption("Python Party")  # name of the window
    screen_game = pygame.display.set_mode((600,  600))  # size of the window
    background_game = pygame.image.load('plateau_python_party.png')  # import board game on the window
    background_game = pygame.transform.scale(background_game, (600, 600))  # resie the picture
    screen_game.blit(background_game, (0, 0))  # update the window with the picture inside
    pygame.display.flip()

    # dictionary which allow us to transfer and save important data
    data = {
        'player_1_pos': 0,
        'player_2_pos': 0,
        'player_1_turn': 0,
        'player_2_turn': 0,
    }

    # try to open the file with data
    try:
        with open('players_pos.txt') as score_file:
            data = json.load(score_file)
    except:
        print('No file created yet')  # if there is no file created yet

    # variable
    score = 0  # for loop function
    pion_1 = pygame.image.load('caracteres_1.png')  # pawn for player 1
    pion_1 = pygame.transform.scale(pion_1, (40, 40))
    pion_2 = pygame.image.load('caracteres_2.png')  # pawn for player 2
    pion_2 = pygame.transform.scale(pion_2, (40, 40))
    coin_flip_rules = pygame.image.load('coin_flip_rule.png')  # picture of coinflip game rule
    clicker_rule = pygame.image.load ('clicker_rule.png')  # picture of clicker game rule

    def roll_dice(result):
        """
The function makes a little animation for the dice rolling then show the result and send back the result.
        :param result: result of die roll
        :return: a random corresponding to the result of the dice rolling allocate to x
        """
        color = (170, 170, 170)
        roll_button = pygame.draw.rect(screen_game, color, pygame.Rect(250, 400, 50, 30))
        small_font = pygame.font.SysFont('Corbel', 35)
        text = small_font.render('Roll', True, (0, 0, 0))
        screen_game.blit(text, (250, 400))
        pygame.display.flip()

        loop = True

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if roll_button.collidepoint(event.pos):
                        counter = 0
                        while counter < 10:  # loop which show a random face of the dice to simulate a die rolling
                            number = random.randint(1, 6)
                            if number == 1:  # if the result is 1 it loads the face number 1, same for 2...
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

                        if number == 1:  # loop to show the final result
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
                        loop = False
        result = number
        return result

    def dice_result(result_roll_dice):
        """
Show the result of die rolling. Allow us to reload the screen and still having the result on the window
        :param result_roll_dice: insert the result of the roll_dice function
        """
        if result_roll_dice == 1:
            dice_rolled = pygame.image.load('dé_1.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        elif result_roll_dice == 2:
            dice_rolled = pygame.image.load('dé_2.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        elif result_roll_dice == 3:
            dice_rolled = pygame.image.load('dé_3.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        elif result_roll_dice == 4:
            dice_rolled = pygame.image.load('dé_4.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        elif result_roll_dice == 5:
            dice_rolled = pygame.image.load('dé_5.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        else:
            dice_rolled = pygame.image.load('dé_6.jpg')
            screen_game.blit(dice_rolled, (300, 375))
        pygame.display.flip()

    def player_1_before_movements(player2_loc):
        """
Reload the window with board game and pawn 2 before pawn 1 movement to not have multiple pawn appearing on the window.
        :param player2_loc: current location of pawn 2
        """
        screen_game.blit(background_game, (0, 0))

        # detect the pawn location on screen and put it correctly
        if player2_loc == 0:
            screen_game.blit(pion_2, (60, 128))
        elif player2_loc == 1:
            screen_game.blit(pion_2, (190, 128))
        elif player2_loc == 2:
            screen_game.blit(pion_2, (250, 128))
        elif player2_loc == 3:
            screen_game.blit(pion_2, (310, 128))
        elif player2_loc == 4:
            screen_game.blit(pion_2, (370, 128))
        elif player2_loc == 5:
            screen_game.blit(pion_2, (430, 128))
        elif player2_loc == 6:
            screen_game.blit(pion_2, (460, 160))
        elif player2_loc == 7:
            screen_game.blit(pion_2, (460, 220))
        elif player2_loc == 8:
            screen_game.blit(pion_2, (430, 245))
        elif player2_loc == 9:
            screen_game.blit(pion_2, (370, 245))
        elif player2_loc == 10:
            screen_game.blit(pion_2, (310, 245))
        elif player2_loc == 11:
            screen_game.blit(pion_2, (250, 245))
        elif player2_loc == 12:
            screen_game.blit(pion_2, (190, 245))
        elif player2_loc == 13:
            screen_game.blit(pion_2, (130, 245))
        elif player2_loc == 14:
            screen_game.blit(pion_2, (70, 245))
        elif player2_loc == 15:
            screen_game.blit(pion_2, (70, 305))
        elif player2_loc == 16:
            screen_game.blit(pion_2, (70, 365))
        elif player2_loc == 17:
            screen_game.blit(pion_2, (70, 425))
        elif player2_loc == 18:
            screen_game.blit(pion_2, (70, 485))
        elif player2_loc == 19:
            screen_game.blit(pion_2, (130, 485))
        elif player2_loc == 20:
            screen_game.blit(pion_2, (190, 485))
        elif player2_loc == 21:
            screen_game.blit(pion_2, (250, 515))
        elif player2_loc == 22:
            screen_game.blit(pion_2, (310, 515))
        elif player2_loc == 23:
            screen_game.blit(pion_2, (370, 515))
        elif player2_loc == 24:
            screen_game.blit(pion_2, (430, 515))
        elif player2_loc == 25:
            screen_game.blit(pion_2, (490, 515))
        elif player2_loc > 25:
            screen_game.blit(pion_2, (505, 485))

    def player_1_location(player1_loc):
        """
Put the pawn 1 correctly on the screen.
        :param player1_loc: current location of pawn 1
        """
        if player1_loc == 0:
            screen_game.blit(pion_1, (60, 128))
        elif player1_loc == 1:
            screen_game.blit(pion_1, (190, 128))
        elif player1_loc == 2:
            screen_game.blit(pion_1, (250, 128))
        elif player1_loc == 3:
            screen_game.blit(pion_1, (310, 128))
        elif player1_loc == 4:
            screen_game.blit(pion_1, (370, 128))
        elif player1_loc == 5:
            screen_game.blit(pion_1, (430, 128))
        elif player1_loc == 6:
            screen_game.blit(pion_1, (460, 160))
        elif player1_loc == 7:
            screen_game.blit(pion_1, (460, 220))
        elif player1_loc == 8:
            screen_game.blit(pion_1, (430, 245))
        elif player1_loc == 9:
            screen_game.blit(pion_1, (370, 245))
        elif player1_loc == 10:
            screen_game.blit(pion_1, (310, 245))
        elif player1_loc == 11:
            screen_game.blit(pion_1, (250, 245))
        elif player1_loc == 12:
            screen_game.blit(pion_1, (190, 245))
        elif player1_loc == 13:
            screen_game.blit(pion_1, (130, 245))
        elif player1_loc == 14:
            screen_game.blit(pion_1, (70, 245))
        elif player1_loc == 15:
            screen_game.blit(pion_1, (70, 305))
        elif player1_loc == 16:
            screen_game.blit(pion_1, (70, 365))
        elif player1_loc == 17:
            screen_game.blit(pion_1, (70, 425))
        elif player1_loc == 18:
            screen_game.blit(pion_1, (70, 485))
        elif player1_loc == 19:
            screen_game.blit(pion_1, (130, 485))
        elif player1_loc == 20:
            screen_game.blit(pion_1, (190, 485))
        elif player1_loc == 21:
            screen_game.blit(pion_1, (250, 515))
        elif player1_loc == 22:
            screen_game.blit(pion_1, (310, 515))
        elif player1_loc == 23:
            screen_game.blit(pion_1, (370, 515))
        elif player1_loc == 24:
            screen_game.blit(pion_1, (430, 515))
        elif player1_loc == 25:
            screen_game.blit(pion_1, (490, 515))
        elif player1_loc > 25:
            screen_game.blit(pion_1, (505, 485))

    def player_2_location(player2_loc):
        """
Put correctly the pawn 2 on screen
        :param player2_loc: current location of pawn 2
        """
        if player2_loc == 0:
            screen_game.blit(pion_2, (60, 128))
        elif player2_loc == 1:
            screen_game.blit(pion_2, (190, 128))
        elif player2_loc == 2:
            screen_game.blit(pion_2, (250, 128))
        elif player2_loc == 3:
            screen_game.blit(pion_2, (310, 128))
        elif player2_loc == 4:
            screen_game.blit(pion_2, (370, 128))
        elif player2_loc == 5:
            screen_game.blit(pion_2, (430, 128))
        elif player2_loc == 6:
            screen_game.blit(pion_2, (460, 160))
        elif player2_loc == 7:
            screen_game.blit(pion_2, (460, 220))
        elif player2_loc == 8:
            screen_game.blit(pion_2, (430, 245))
        elif player2_loc == 9:
            screen_game.blit(pion_2, (370, 245))
        elif player2_loc == 10:
            screen_game.blit(pion_2, (310, 245))
        elif player2_loc == 11:
            screen_game.blit(pion_2, (250, 245))
        elif player2_loc == 12:
            screen_game.blit(pion_2, (190, 245))
        elif player2_loc == 13:
            screen_game.blit(pion_2, (130, 245))
        elif player2_loc == 14:
            screen_game.blit(pion_2, (70, 245))
        elif player2_loc == 15:
            screen_game.blit(pion_2, (70, 305))
        elif player2_loc == 16:
            screen_game.blit(pion_2, (70, 365))
        elif player2_loc == 17:
            screen_game.blit(pion_2, (70, 425))
        elif player2_loc == 18:
            screen_game.blit(pion_2, (70, 485))
        elif player2_loc == 19:
            screen_game.blit(pion_2, (130, 485))
        elif player2_loc == 20:
            screen_game.blit(pion_2, (190, 485))
        elif player2_loc == 21:
            screen_game.blit(pion_2, (250, 515))
        elif player2_loc == 22:
            screen_game.blit(pion_2, (310, 515))
        elif player2_loc == 23:
            screen_game.blit(pion_2, (370, 515))
        elif player2_loc == 24:
            screen_game.blit(pion_2, (430, 515))
        elif player2_loc == 25:
            screen_game.blit(pion_2, (490, 515))
        elif player2_loc > 25:
            screen_game.blit(pion_2, (505, 485))

    def player_2_before_movements(player1_loc):
        """
Same utility than the function player_1_before_movement but this is for the pawn 2
        :param player1_loc: current location of pawn 1
        """
        screen_game.blit(background_game, (0, 0))
        if player1_loc == 0:
            screen_game.blit(pion_1, (60, 128))
        elif player1_loc == 1:
            screen_game.blit(pion_1, (190, 128))
        elif player1_loc == 2:
            screen_game.blit(pion_1, (250, 128))
        elif player1_loc == 3:
            screen_game.blit(pion_1, (310, 128))
        elif player1_loc == 4:
            screen_game.blit(pion_1, (370, 128))
        elif player1_loc == 5:
            screen_game.blit(pion_1, (430, 128))
        elif player1_loc == 6:
            screen_game.blit(pion_1, (460, 160))
        elif player1_loc == 7:
            screen_game.blit(pion_1, (460, 220))
        elif player1_loc == 8:
            screen_game.blit(pion_1, (430, 245))
        elif player1_loc == 9:
            screen_game.blit(pion_1, (370, 245))
        elif player1_loc == 10:
            screen_game.blit(pion_1, (310, 245))
        elif player1_loc == 11:
            screen_game.blit(pion_1, (250, 245))
        elif player1_loc == 12:
            screen_game.blit(pion_1, (190, 245))
        elif player1_loc == 13:
            screen_game.blit(pion_1, (130, 245))
        elif player1_loc == 14:
            screen_game.blit(pion_1, (70, 245))
        elif player1_loc == 15:
            screen_game.blit(pion_1, (70, 305))
        elif player1_loc == 16:
            screen_game.blit(pion_1, (70, 365))
        elif player1_loc == 17:
            screen_game.blit(pion_1, (70, 425))
        elif player1_loc == 18:
            screen_game.blit(pion_1, (70, 485))
        elif player1_loc == 19:
            screen_game.blit(pion_1, (130, 485))
        elif player1_loc == 20:
            screen_game.blit(pion_1, (190, 485))
        elif player1_loc == 21:
            screen_game.blit(pion_1, (250, 515))
        elif player1_loc == 22:
            screen_game.blit(pion_1, (310, 515))
        elif player1_loc == 23:
            screen_game.blit(pion_1, (370, 515))
        elif player1_loc == 24:
            screen_game.blit(pion_1, (430, 515))
        elif player1_loc == 25:
            screen_game.blit(pion_1, (490, 515))
        elif player1_loc > 25:
            screen_game.blit(pion_1, (505, 485))

    def action_player_1(player1_loc):
        """
Detect the current location of the pawn 1 and apply case effect
        :param player1_loc: current location of pawn 1
        """
        if player1_loc == 1:
            bonus = random.randint(0, 1)  # generate the number of case you can move forward
            player1_loc += bonus
        elif player1_loc == 2:
            with open('players_pos.txt', 'w') as score_file: # save our data in a file to reload it when we launch the game
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))  # show the rule of the clicker game
            pygame.display.flip()
            pygame.time.delay(5000)  # delay before the launching of the game to have time to read rule
            pygame.display.quit()
            clicker_game()
        elif player1_loc == 3:
            malus = random.randint(1, 2)  # generate the number of case you can go back
            player1_loc -= malus
        elif player1_loc == 4:
            bonus = random.randint(1, 3)
            player1_loc += bonus
        elif player1_loc == 6:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))  # show rule of the coinflip game before launching it
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player1_loc == 7:
            bonus = random.randint(1, 3)
            player1_loc += bonus
        elif player1_loc == 9:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player1_loc == 11:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player1_loc == 12:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player1_loc == 13:
            bonus = random.randint(1, 3)
            player1_loc += bonus
        elif player1_loc == 15:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player1_loc == 16:
            malus = random.randint(1, 3)
            player1_loc -= malus
        elif player1_loc == 17:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player1_loc == 18:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player1_loc == 19:
            malus = random.randint(1, 3)
            player1_loc -= malus
        elif player1_loc == 21:
            bonus = random.randint(1, 1)
            player1_loc += bonus
        elif player1_loc == 22:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player1_loc == 23:
            malus = random.randint(1, 3)
            player1_loc -= malus
        elif player1_loc == 24:
            malus = random.randint(1, 3)
            player1_loc -= malus
        elif player1_loc == 25:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()


    def action_player_2(player2_loc):
        """
Detect the current location of the pawn 2 and apply case effect
        :param player2_loc: current location of pawn 2
        """
        if player2_loc == 1:
            bonus = random.randint(0, 1)
            player2_loc += bonus
        elif player2_loc == 2:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player2_loc == 3:
            malus = random.randint(1, 2)
            player2_loc -= malus
        elif player2_loc == 4:
            bonus = random.randint(1, 3)
            player2_loc += bonus
        elif player2_loc == 6:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player2_loc == 7:
            bonus = random.randint(1, 3)
            player2_loc += bonus
        elif player2_loc == 9:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player2_loc == 11:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player2_loc == 12:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player2_loc == 13:
            bonus = random.randint(0, 1)
            player2_loc += bonus
        elif player2_loc == 15:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player2_loc == 16:
            malus = random.randint(1, 3)
            player2_loc -= malus
        elif player2_loc == 17:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player2_loc == 18:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()
        elif player2_loc == 19:
            malus = random.randint(1, 3)
            player2_loc -= malus
        elif player2_loc == 21:
            bonus = random.randint(0, 1)
            data['player_2_pos'] += bonus
        elif player2_loc == 22:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(coin_flip_rules, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            coin_flip_game()
        elif player2_loc == 23:
            malus = random.randint(1, 3)
            player2_loc -= malus
        elif player2_loc == 24:
            malus = random.randint(1, 3)
            player2_loc -= malus
        elif player2_loc == 25:
            with open('players_pos.txt', 'w') as score_file:
                json.dump(data, score_file)
            screen_game.blit(clicker_rule, (0, 0))
            pygame.display.flip()
            pygame.time.delay(5000)
            pygame.display.quit()
            clicker_game()

    # condition for the game to continue

    while data['player_1_pos'] <= 25 and data['player_2_pos'] <= 25:

        # initialize pawn's start locations
        player_1_location(data['player_1_pos'])
        player_2_location(data['player_2_pos'])

        # turn of player 1 if the condition is true

        if data['player_1_turn'] == data['player_2_turn']:

            # roll die and player 1 movement
            result_1 = roll_dice(score)  # allocate result of the roll to a variable
            data['player_1_pos'] += result_1  # add the result to the player location to be able to move it

            # calling the next functions to don't have multiple pawn 1 on window

            player_1_before_movements(data['player_2_pos'])  # call the function
            dice_result(result_1)  # call the function
            player_1_location(data['player_1_pos'])  # pawn 1 location

            # player 1 turn counter
            data['player_1_turn'] += 1

            # bonus/malus or game for player 1
            action_player_1(data['player_1_pos'])

            # call these function to move pawn 1 without getting multiple pawn 1 if we get a bonus/malus case
            player_1_before_movements(data['player_2_pos'])
            dice_result(result_1)
            player_1_location(data['player_1_pos'])

        # turn of player 2 if the condition is true

        elif data['player_1_turn'] > data['player_2_turn']:

            # roll dice and player 2 movement
            result_2 = roll_dice(score)
            data['player_2_pos'] += result_2
            player_2_before_movements(data['player_1_pos'])
            dice_result(result_2)
            player_2_location(data['player_2_pos'])

            # turn counter player 2
            data['player_2_turn'] += 1

            # bonus/malus or game player 2
            action_player_1(data['player_2_pos'])
            player_2_before_movements(data['player_1_pos'])
            dice_result(result_2)
            player_2_location(data['player_2_pos'])

    # player 1 winner if condition is true
    if data['player_1_pos'] > 25:
        win_screen = pygame.image.load ('caracteres_1_win.png')  # show victory screen for player 1
        screen_game.blit(win_screen, (0, 0))
        pygame.display.flip()
    else:
        win_screen = pygame.image.load('caracteres_2_win.png') # show victory screen for player 2
        screen_game.blit(win_screen, (0, 0))
        pygame.display.flip()
        pygame.display.flip()

    boucle = True

    while boucle:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                boucle = False
                pygame.quit()
        pygame.display.flip()