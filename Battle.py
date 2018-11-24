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


def fight(battle_factions: list):
    global factions
    soldiers = [faction.pick_soldier() for faction in battle_factions]

    for index, soldier in enumerate(soldiers):
        for enemyIndex, enemy in enumerate(soldiers):
            if index <= enemyIndex:
                continue
            soldier_strike = soldier.calculate_strike()
            enemy_strike = enemy.calculate_strike()

            if soldier_strike < enemy_strike:
                print('Hermaður frá {} með högg {} '
                      'vinnur hermann frá {} með '
                      'högg {}'.format(enemy.faction.name, round(enemy_strike, 2), soldier.faction.name, round(soldier_strike, 2)))
                soldier.hp -= 1
                if soldier.hp <= 0:
                    soldier.faction.kia(soldier)
                    if soldier.faction.defeated:
                        factions.remove(soldier.faction)
            if soldier_strike > enemy_strike:
                print('Hermaður frá {} með högg {} '
                      'vinnur hermann frá {} með '
                      'högg {}'.format(soldier.faction.name, round(enemy_strike, 2), enemy.faction.name, round(soldier_strike, 2)))
                soldier.hp -= 1
                if enemy.hp <= 0:
                    enemy.faction.kia(enemy)
                    if enemy.faction.defeated:
                        factions.remove(soldier.faction)


def main():
    global factions
    factions = create_factions()

    while True:
        if len(factions) > 1:
            fight(random.sample(factions, 2))
            # TODO Fjarlæga faction úr lista þegar allir meðlimir eru dánir
        else:
            print('Ættbálkurinn {} vann!'.format(factions[0].name))
            break


factions = []
if __name__ == '__main__':
    main()



