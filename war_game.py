import random
from time import sleep


class Warrior:
    def __init__(self, name='anon', stamina=0, attack_points=0, defence_points=0):
        self.name = name
        self.stamina = stamina
        self.attack_points = attack_points
        self.defence_points = defence_points

    def attack(self):
        return random.randint(0, self.attack_points)*random.randint(2, 5)

    def defence(self):
        return random.randint(0, self.defence_points)

    def lost_stamina(self, amount):
        self.stamina -= amount
        if self.stamina <= 0:
            print(f'{self.name} died in battle')

    def still_alive(self):
        if self.stamina <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.name


def fight(player1, player2):
    i = 1
    while player1.still_alive() and player2.still_alive():
        print('Round: ', i)
        show_stats(player1, player2)

        if random.randint(0, 1) == 0:
            battle(player1, player2)
        else:
            battle(player2, player1)

        print('')
        sleep(5)
        i += 1

    if player2.still_alive():
        print(f"{player2.name} has won the fight")
    else:
        print(f"{player1.name} has won the fight")


def battle(x, y):
    print(f"{x.name} has been attacked by {y.name}")
    injuries = y.attack() - x.defence()
    if injuries <= 0:
        print(f"{x.name} regenerated {-injuries} of stamina")
    else:
        print(f"{x.name} lost {injuries} points of live")
    x.lost_stamina(injuries)


def show_stats(x, y):
    for player in (x, y):
        print(f"{player.name} has {player.stamina} stamina left")


player_name1 = input("Enter the name of the first player: ")
player_name2 = input("Enter the name of the second player: ")

player1 = Warrior(player_name1, random.randint(100, 1000), random.randint(10, 50), random.randint(5, 30))
player2 = Warrior(player_name2, random.randint(100, 1000), random.randint(10, 50), random.randint(5, 30))


fight(player1, player2)
