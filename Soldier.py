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

    def __str__(self):
        return self.is_super  # TODO Þarf að útfæra þennan klasa

    def __repr__(self):
        return str(self.is_super)


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
            raise NotImplemented
        return random.choice(self.soldiers)

    def kia(self, soldier):
        self.soldiers.remove(soldier)
        if len(self.soldiers) == 0:
            self.defeated = True


if __name__ == '__main__':
    f1 = Faction('Dude', 7, 3)
    print(f1.soldiers)
