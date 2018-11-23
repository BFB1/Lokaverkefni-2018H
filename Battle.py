# Baldur Fróði Briem
# 22/11/2018
import Soldier
import random


def create_factions():
    factions = []
    for faction in ['Pessar', 'Hettir', 'Dreyrar']:
        regular_soldiers = get_integer_from_user('Hversu margir venjulegir hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        super_soldiers = get_integer_from_user('Hversu margir super hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        factions.append(Soldier.Faction(faction, regular_soldiers, super_soldiers))
    return factions


def get_integer_from_user(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Hér þarf að slá inn tölu')


def fight(factions: list):
    soldiers = [faction.pick_soldier() for faction in factions]

    for index, soldier in enumerate(soldiers):
        for enemyIndex, enemy in enumerate(soldiers):
            if index <= enemyIndex:
                continue
            soldier_strike = soldier.calculate_strike()
            enemy_strike = enemy.calculate_strike()

            if soldier_strike < enemy_strike:
                print('Hermaður frá {} með högg {}'
                      'vinnur hermann frá {} með '
                      'högg {}'.format(enemy.faction.name, round(enemy_strike, 2), soldier.faction.name, round(soldier_strike)))
                soldier.hp -= 1
                if soldier.hp <= 0:
                    soldier.die()


def main():
    factions = create_factions()

    while True:
        fight(random.sample(factions, 2))
        # TODO Fjarlæga faction úr lista þegar allir meðlimir eru dánir




if __name__ == '__main__':
    main()



