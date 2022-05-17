import pygame
from pygame.locals import *

pygame.init()

# initialisation de la fenêtre de jeu
fenetre = pygame.display.set_mode((600, 600))

# écran d'accueil
fond = pygame.image.load('écran_accueil_ebauche.png')
fenetre.blit(fond, (0, 0))

# Actualise l'écran
pygame.display.flip()

# détection d'évènements en jeu (cliquesouris/clavier, fermer la fenêtre,...) et réaction en fonction
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
