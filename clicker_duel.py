import pygame
import json
import random

pygame.init()

def clicker_game():
    pygame.display.set_caption('Clicker')
    screen = pygame.display.set_mode((600, 600))
    screen.fill((255, 255, 255))

    try:
        with open('players_pos.txt') as score_file:
            data = json.load(score_file)
    except:
        print('No file created yet')


    small_font = pygame.font.SysFont('Corbel', 35)
    player_1 = small_font.render('player_1', True, (0, 0, 0))
    screen.blit(player_1, (50, 50))
    player_2 = small_font.render('player_2', True, (0, 0, 0))
    screen.blit(player_2, (400, 50))
    key_1 = small_font.render('press S', True, (0, 0, 0))
    screen.blit(key_1, (50, 150))
    key_2 = small_font.render('press K', True, (0, 0, 0))
    screen.blit(key_2, (400, 150))
    counter_1 = 0
    counter_2 = 0

    pygame.display.flip()

    while True:
        while counter_1 < 50 and counter_2 < 50:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(70, 200, 100, 100))
                        counter_1 += 1
                        text_1 = small_font.render(str(counter_1), True, (0, 0, 0))
                        screen.blit(text_1, (70, 200))
                    if event.key == pygame.K_k:
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(400, 200, 100, 100))
                        counter_2 += 1
                        text_2 = small_font.render(str(counter_2), True, (0, 0, 0))
                        screen.blit(text_2, (400, 200))
                    pygame.display.flip()
        break

    if counter_1 < counter_2 :
        win_text_1 = small_font.render('Player 2 won', True, (0, 0, 0))
        screen.blit(win_text_1, (200, 300))
        number = random.randint(1, 3)
        data['player_2_pos'] += number
    else:
        win_text_2 = small_font.render('Player 1 won', True, (0, 0, 0))
        screen.blit(win_text_2, (200, 300))
        number_2 = random.randit(1,3)
        data['player_1_pos'] += number_2
    pygame.display.flip()

    with open ('players_pos','w') as score_file:
        json.dump(data, score_file)
    pygame.display.quit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

