import pygame
pygame.init()

#initialisation de la fenêtre de jeu
pygame.display.set_caption("Python Parthy")
screen = pygame.display.set_mode((600,  600))
background = pygame.image.load('écran_accueil_ebauche.png')

screen.blit(background, (0, 0)) #applique le background à la fenêtre

#bouton nouvelle partie
color = (170, 170, 170)
pygame.draw.rect(screen, color, pygame.Rect(150, 300, 300, 50))
smallfont = pygame.font.SysFont('Corbel',35)
text = smallfont.render('New Game', True, (0, 0, 0))
screen.blit(text, (233, 310))



pygame.display.flip() #mettre à jour la fenêtre



running = True

#boucle tant que cette condition est vrai
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


