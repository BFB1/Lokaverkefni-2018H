# Baldur Fróði Briem
# 22/11/2018
import Soldier
import random
import time

from Soldier import get_integer_from_user


def create_factions():
    """
    Þetta fall tekur inn frá notanda hversu marga hermenn hann vill í hverjum ættbálk og hvort hann vilji stjórna honum
    og skilar lista með öllum ættbálkunum

    :return: list[Faction]
    """
    factions = []
    for faction in ['Pessar', 'Hettir', 'Dreyrar']:
        regular_soldiers = get_integer_from_user(
            'Hversu margir venjulegir hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        super_soldiers = get_integer_from_user(
            'Hversu margir super hermenn eiga að vera í ættbálkinum {}? '.format(faction))
        user_control = True if input('Vilt þú stjórna ættbálkinum[Y/N]? ').upper() == 'Y' else False
        factions.append(Soldier.Faction(faction, regular_soldiers, super_soldiers, user_control))
    return factions


def damage(soldier):
    """
    Þetta fall sér um að draga frá heilsu hermanns og passa svo uppá að fjarlæga hann úr leiknum ef hann er dáinn
    og ættbálkinn hans ef hann var síðasti hermaðurinn í ættbálkinum.

    :param soldier: Soldier
    :return: None
    """
    soldier.hp -= 1
    if soldier.hp <= 0:
        soldier.faction.kia(soldier)
        if soldier.faction.defeated:
            factions.remove(soldier.faction)


def fight(battle_factions: list):
    """
    Þetta fall framkvæmir slagsmál milli hermanna. Það tekur inn lista af ættbálkum sem eiga að slást.
    Síðan eru ættbálkarnir beðnir um að velja hermann til þess að berjast og þeir settir í lista.
    Svo eru valdir hermenn úr listanum og reiknað út höggið þeirra. Sá sem er með hærra högg vinnur.
    Þá þarf að draga líf frá hinum hermanninum og svo er loks skilað streng sem segir hvað gerðist í slagsmálunum

    :param battle_factions: list[Faction]
    :return: str
    """
    global factions
    soldiers = [faction.pick_soldier() for faction in battle_factions]

    for index, soldier in enumerate(soldiers):
        for enemyIndex, enemy in enumerate(soldiers):
            if index <= enemyIndex:
                continue
            soldier_strike = soldier.calculate_strike()
            enemy_strike = enemy.calculate_strike()

            if soldier_strike < enemy_strike:
                damage(soldier)
                return ('{} með högg {} '
                        'vinnur {} með '
                        'högg {}. Hann er nú með {} líf'.format(enemy.name, round(enemy_strike, 2), soldier.name,
                                                                round(soldier_strike, 2), soldier.hp))
            if soldier_strike > enemy_strike:
                damage(enemy)
                return ('{} með högg {} '
                        'vinnur {} með '
                        'högg {}. Hann er nú með {} líf'.format(soldier.name, round(soldier_strike, 2), enemy.name,
                                                                round(enemy_strike, 2), enemy.hp))
            else:
                return 'Jafntefli'


def main():
    """
    Aðalfallið. Setur upp og stýrir framvindu leiksins.

    :return: None
    """
    global factions
    factions = create_factions()

    print('\nLeikreglur\n'
          'Nú munu þessir ættbálkar berjast við hvorn annan þangað til að einn stendur eftir sem sigurvegari.\n'
          'Bardaginn fer þannig fram að í hverri umferð senda tveir af ættbálkunum einn hermann í slagsmál.\n'
          'Högg hermannanna er reiknað út frá vopni, afli hermannana, og heppni.\n'
          'Sá hermaður sem er með hærra "högg" vinnur bardagan og þá missir hinn eitt líf.\n'
          'Þegar allir hermenn í ættbálk eru dánir þá telst ættbálkurinn sigraður.\n'
          'Leiknum líkur þegar að bara einn ættbálkur er eftir\n')

    rounds = 0
    while True:
        if len(factions) > 1:
            rounds += 1

            try:
                print(fight(random.sample(factions, 2)))
            except IndexError:
                print([faction.soldiers for faction in factions])

            # Í hverri fimmtu umferð þá er prentuð út staða leiksins
            if rounds % 5 == 0:
                print('\nStaðan')
                for faction in factions:
                    if faction.defeated:
                        print('{} er sigraður'.format(faction.name))
                    else:
                        print(faction.name)
                        print('Fjöldi hermanna: {}'.format(faction.number_of_soldiers))
                        print('Samanlögð líf hermanna: {}'.format(faction.total_hit_points_of_soldiers))
                        print('Fjöldi súperhermanna: {}'.format(faction.number_of_super_soldiers))
                        print('Samanlögð líf súperhermanna: {}'.format(faction.total_hit_points_of_super_soldiers))
                        print('Samanlögð stærð ættbálksins: {}'.format(faction.total_army_size))
                        print('Samanlögð líf ættbálksins: {}\n'.format(faction.total_army_hit_points))

            time.sleep(1)

        else:
            return 'Ættbálkurinn {} vann!'.format(factions[0].name)


# Þetta kallar á main() fallið ef þessi skrá er keyrð
if __name__ == '__main__':
    factions = []
    print(main())
