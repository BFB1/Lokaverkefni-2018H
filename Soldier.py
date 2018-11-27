# Baldur Fróði Briem
# 22/11/2018
import random


class Soldier:

    # Færa gögn inn í hlutinn
    def __init__(self, hp, weapon_type, power, is_super, faction):
        self.hp = hp
        self.weapon_type = weapon_type
        self.power = power
        self.is_super = is_super
        self.faction = faction

    # Reikna út högg frá þessum hermanni
    # Högg hermannsins í bardaga er afl hermannsins margfaldað með aflbreyti vopsins
    # og aflbreyti frá heppni.
    def calculate_strike(self):

        # Reikna út aflbreyti vopsins
        # Sverð er meðalvopn
        if self.weapon_type == 1:
            weapon_modifier = 1
        # Spjót er lélegt vopn
        elif self.weapon_type == 2:
            weapon_modifier = 0.75
        # Exi er gott vopn
        else:
            weapon_modifier = 1.25

        # Búa til og skila afli hermansins breyttu fyrir vopn og heppni
        return weapon_modifier * self.power * random.uniform(0.75, 1.25)

    @property
    def name(self):
        return '{}{}'.format('Super' if self.is_super else '', self.faction.name)

    def __str__(self):
        return 'Nafn = {} Líf = {} Vopn = {} Afl = {}'.format(self.name, self.hp, self.weapon_type, self.power)

    def __repr__(self):
        return self.__str__()


class Faction:

    def __init__(self, name, number_of_soldiers, number_of_super_soldiers, user_controlled=False):
        self.name = name
        self.userControlled = user_controlled
        self.defeated = False

        self.soldiers = [Faction.generate_soldier(self, False) for i in range(number_of_soldiers)]
        self.soldiers += [Faction.generate_soldier(self, True) for i in range(number_of_super_soldiers)]

    def generate_soldier(self, is_super):
        if is_super:
            return Soldier(random.randint(10, 15), random.randint(1, 3), random.randint(4, 9), True, self)
        else:
            return Soldier(random.randint(1, 5), random.randint(1, 3), random.randint(1, 5), False, self)

    def pick_soldier(self):
        if self.userControlled:
            for index, soldier in enumerate(self.soldiers):
                print('{}. {}'.format(index + 1, soldier))
            while True:
                try:
                    selected_soldier = self.soldiers[get_integer_from_user('Sláðu inn tölu hermanns: ') + 1]
                except IndexError:
                    print('Enginn hermaður fannst með þessa tölu')
                    continue
                break
            return selected_soldier
        else:
            return random.choice(self.soldiers)

    def kia(self, soldier):
        self.soldiers.remove(soldier)
        if len(self.soldiers) == 0:
            self.defeated = True

    @property
    def number_of_soldiers(self):
        return len([soldier for soldier in self.soldiers if not soldier.is_super])

    @property
    def total_hit_points_of_soldiers(self):
        return sum([soldier.hp for soldier in self.soldiers if not soldier.is_super])

    @property
    def number_of_super_soldiers(self):
        return len([soldier for soldier in self.soldiers if soldier.is_super])

    @property
    def total_hit_points_of_super_soldiers(self):
        return sum([soldier.hp for soldier in self.soldiers if soldier.is_super])

    @property
    def total_army_size(self):
        return len(self.soldiers)

    @property
    def total_army_hit_points(self):
        return sum([soldier.hp for soldier in self.soldiers])


def get_integer_from_user(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Hér þarf að slá inn tölu')


if __name__ == '__main__':
    f1 = Faction('Dude', 7, 3)
    print(f1.soldiers)
