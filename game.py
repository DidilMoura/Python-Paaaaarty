import pygame

def game():

    pygame.display.set_caption("Python Parthy")
    screen_game = pygame.display.set_mode((600,  600))
    background_game = pygame.image.load('plateau_python_party.png')
    screen_game.blit(background_game, (0, 0))



    pygame.display.flip()

    running = True


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
