from random import randint


class Choice:

    def __init__(self):
        return

    def bonus_or_malus(self):

        self.choice = randint(0, 1)

        if self.choice == 0:
            return Bonus
        else:
            return Malus


class Bonus:

    def __init__(self):

        print('Le gagnant aura un BONUS de déplacement !!')

        self.bonus = randint(1, 3)

        if self.bonus == 1:
            print('Vous avancez de ' + str(self.bonus) + ' case')
        else:
            print('Vous avancez de ' + str(self.bonus) + ' cases')


class Malus:

    def __init__(self):

        print('Le perdant aura un MALUS de déplacement !!')

        self.malus = randint(1, 3)

        if self.malus == 1:
            print('Vous reculez de ' + str(self.malus) + ' case')
        else:
            print('Vous reculez de ' + str(self.malus) + ' cases')


choice = Choice()
bom = choice.bonus_or_malus()
bonus = Bonus()
malus = Malus()
