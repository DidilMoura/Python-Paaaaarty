import pygame
pygame.init()
from game import game

#initialisation de la fenêtre de jeu
pygame.display.set_caption("Python Party")
screen = pygame.display.set_mode((600,  600))
background = pygame.image.load('écran_accueil_ebauche.png')

screen.blit(background, (0, 0)) #applique le background à la fenêtre

#bouton nouvelle partie
color = (170, 170, 170)
new_game_button = pygame.draw.rect(screen, color, pygame.Rect(150, 300, 300, 50))
small_font = pygame.font.SysFont('Corbel', 35)
text = small_font.render('New Game', True, (0, 0, 0))
screen.blit(text, (233, 310))



pygame.display.flip() #mettre à jour la fenêtre



running = True

#boucle tant que cette condition est vrai
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_game_button.collidepoint(event.pos):
                pygame.display.quit()
                game()






