import pygame
from game import game

pygame.init()

# home game window
pygame.display.set_caption("Python Party")
screen = pygame.display.set_mode((600,  600))
background = pygame.image.load('écran_accueil_ebauche.png')

screen.blit(background, (0, 0))  # apply background to window

# new game button
color = (170, 170, 170)
new_game_button = pygame.draw.rect(screen, color, pygame.Rect(150, 300, 300, 50))
small_font = pygame.font.SysFont('Corbel', 35)
text = small_font.render('New Game', True, (0, 0, 0))
screen.blit(text, (233, 310))

pygame.display.flip()  # update current window

running = True

# infinite loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # detect if someone close the window
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_game_button.collidepoint(event.pos):  # detect if someone clicks on the button 'new game'
                pygame.display.quit()
                game()






