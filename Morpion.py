import pygame
import sys

class Grille :

    def __init__(self,ecran):
        self.ecran = ecran
        self.lignes = [((200,0),(200,600)),     # création des lignes
                       ((400,0),(400,600)),     # (point de départ),(point d'arrivée)
                       ((0,200),(600,200)),
                       ((0,400),(600,400)),]

    #initiation de la grille
        self.grille = [[None for x in range(0,3)]for y in range(0,3)]

# print la grille
    def print_grille(self):
        print(self.grille)

# fixer les valeurs
    def fixer_la_valeur(self,x,y,valeur):
        self.grille[y][x]=valeur


    def afficher(self):

        for ligne in self.lignes :

            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)    # print la grille
            # couleur, position de départ, position de fin, épaisseur
class Jeu :

    def __init__(self):

        self.ecran = pygame.display.set_mode((600,600))  # taille de l'écran
        pygame.display.set_caption('Le Python Morpion')
        self.jeu_encours = True

        self.grille = Grille(self.ecran)                # création d'une instance de la grille dans la classe Jeu

    # fixer les variables 'X' et 'O'
        self.player_X = 'X'
        self.player_O = 'O'

    #fixer le compteur
        self.compteur = 0

    def fonction_principale(self):

        while self.jeu_encours:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()
                #ajout de l'évènement qui correspond au clic droit
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

                #obtenir la position de la souris
                    position = pygame.mouse.get_pos()
                    position_x ,position_y = position[0]//200 ,position[1]//200     # permet de définir des coordonnées simples et uniformes à chaque case de la grille
                    print(position_x,position_y)

                    self.grille.fixer_la_valeur(position_x,position_y,'X')

                # condition si le compteur de tour est pair ou impair
                    print(self.compteur, self.compteur / 2)
                    if self.compteur / 2 == 0:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_X)

                    else: self.grille.fixer_la_valeur(position_x, position_y, self.player_O)

                    self.compteur += 1

                self.grille.print_grille()

            self.ecran.fill((240,240,240))      # couleur de l'écran

            self.grille.afficher()              # appel de la fonction afficher pour la grille

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    game = Jeu()                 # création d'un objet du type Jeu()
    game.fonction_principale()   # appel de la fonction principale
    pygame.quit()
