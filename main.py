import pygame
import sys

class Grille :

    def __init__(self,ecran):
        self.ecran = ecran
        self.lignes = [((200,0),(200,600)),     # création des lignes
                       ((400,0),(400,600)),     # (point de départ),(point d'arrivée)
                       ((0,200),(600,200)),
                       ((0,400),(600,400)),]

    def afficher(self):

        for ligne in self.lignes :

            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)    # couleur, position de départ, position de fin, épaisseur

class Jeu :

    def __init__(self):

        self.ecran = pygame.display.set_mode((600,600))  # taille de l'écran
        pygame.display.set_caption('Le Python Morpion')
        self.jeu_encours = True

        self.grille = Grille(self.ecran)                # création d'une instance de la grille dans la classe Jeu

    def fonction_principale(self):

        while self.jeu_encours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

            self.ecran.fill((240,240,240))      # couleur de l'écran

            self.grille.afficher()              # appel de la fonction afficher pour la grille

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    game = Jeu()                 # création d'un objet du type Jeu()
    game.fonction_principale()   # appel de la fonction principale
    pygame.quit()

