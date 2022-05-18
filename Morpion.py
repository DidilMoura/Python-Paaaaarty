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

    # initiation d'une variable pour vérifier si le compteur est 'ON'
        self.compteur_on = False

# print la grille
    def print_grille(self):
        print(self.grille)

# fixer les valeurs
    def fixer_la_valeur(self,x,y,valeur):

    # condition si une case possède la valeur None
        if self.grille[y][x] == None :
            self.grille[y][x] = valeur
            # le compteur est ON
            self.compteur_on = True


    def afficher(self):

        for ligne in self.lignes :

            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)    # print la grille
            # couleur, position de départ, position de fin, épaisseur

        # afficher les X et O

        for y in range(0,len(self.grille)):
            for x in range(0,len(self.grille)):
                if self.grille[y][x] == 'X':

                    pygame.draw.line(self.ecran, (0, 0, 0), (x * 200, y * 200), (200 + (x * 200), 200 + (y * 200)), 3)
                    pygame.draw.line(self.ecran, (0, 0, 0), ((x * 200), 200 + (y * 200)), (200 + (x * 200), (y * 200)),
                                     3)

                elif self.grille[y][x] == 'O':

                    pygame.draw.circle(self.ecran, (0, 0, 0), (100 + (x * 200), 100 + (y * 200)), 85, 3)

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
                #ajout de l'évènement qui correspond au clic gauche
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

                #obtenir la position de la souris
                    position = pygame.mouse.get_pos()
                    position_x ,position_y = position[0]//200 ,position[1]//200     # permet de définir des coordonnées simples et uniformes à chaque case de la grille

                # condition si le compteur de tour est pair ou impair
                    if self.compteur % 2 == 0:
                        self.grille.fixer_la_valeur(position_x, position_y, self.player_X)

                    else: self.grille.fixer_la_valeur(position_x, position_y, self.player_O)

                # condition si le compteur ON est vrai
                    if self.grille.compteur_on:
                        self.compteur += 1
                        # fixer la vameur de compteur_on à Faux
                        self.grille.compteur_on = False

        # recherche du gagnant de la partie

            liste_X = []
            liste_O = []
            liste_lignes_X = []
            liste_lignes_O = []
            liste_colonnes_X = []
            liste_colonnes_O = []

            for ligne in range(0,len(self.grille.grille)):
                for colonne in range (0, len(self.grille.grille)):

                    if self.grille.grille[ligne][colonne]== 'X':

                        X_position = (ligne,colonne)
                        liste_X.append(X_position)

                    elif self.grille.grille[ligne][colonne]== 'O':

                        O_position = (ligne,colonne)
                        liste_O.append(O_position)
                        
        # condition de victoire pour X
            if len(liste_X) >= 3:
                for (ligne,colonne) in liste_X:
                    liste_lignes_X.append(ligne)
                    liste_colonnes_X.append(colonne)

            # condition de victoire horizontale
                if liste_lignes_X.count(0) == 3 or liste_lignes_X.count(1) == 3 or liste_lignes_X.count(2) == 3 :
                    print('X a Gagner !!')
                    return exit

            # condition de victoire verticale
                if liste_colonnes_X.count(0) == 3 or liste_colonnes_X.count(1) == 3 or liste_colonnes_X.count(2) == 3 :
                    print('X a Gagner !!')
                    return exit

            # condition de victoire en diagonale
                if liste_lignes_X == liste_colonnes_X or liste_lignes_X == liste_colonnes_X[::-1] :
                    print('X a Gagner !!')
                    return exit

        # condition de victoire pour O
            if len(liste_O) >= 3:
                for (ligne,colonne) in liste_O:
                    liste_lignes_O.append(ligne)
                    liste_colonnes_O.append(colonne)

            # condition de victoire horizontale
                if liste_lignes_O.count(0) == 3 or liste_lignes_O.count(1) == 3 or liste_lignes_O.count(2) == 3 :
                    print('O a Gagner !!')
                    return exit

            # condition de victoire verticale
                if liste_colonnes_O.count(0) == 3 or liste_colonnes_O.count(1) == 3 or liste_colonnes_O.count(2) == 3 :
                    print('O a Gagner !!')
                    return exit

            # condition de victoire en diagonale
                if liste_lignes_O == liste_colonnes_O or liste_lignes_O == liste_colonnes_O[::-1] :
                    print('O a Gagner !!')
                    return exit

                self.grille.print_grille()

            self.ecran.fill((240,240,240))      # couleur de l'écran

            self.grille.afficher()              # appel de la fonction afficher pour la grille

            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    game = Jeu()                 # création d'un objet du type Jeu()
    game.fonction_principale()   # appel de la fonction principale
    pygame.quit()

# Le morpion est terminé
#Il faudrait ajouter des conditions pour le lié au jeux principal !
