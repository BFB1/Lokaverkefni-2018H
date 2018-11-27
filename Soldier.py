# Baldur Fróði Briem
# 22/11/2018
import random


class Soldier:
    """
    Hermaður. Inniheldur breytur og föll tengd hermönnum.
    """

    # Færa gögn inn í hlutinn
    def __init__(self, hp, weapon_type, power, is_super, faction):
        """
        Fallið tekur inn upplýsingar um tilvikið og setur inn í tilviksbreytur

        :param hp: int
        :param weapon_type: int
        :param power: int
        :param is_super: bool
        :param faction: Faction
        """
        self.hp = hp
        self.weapon_type = weapon_type
        self.power = power
        self.is_super = is_super
        self.faction = faction

    def calculate_strike(self):
        """
        Reikna út högg frá þessum hermanni
        Högg hermannsins í bardaga er afl hermannsins margfaldað með aflbreyti vopsins
        og aflbreyti frá heppni.

        :return: int
        """

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
        """
        Skilar ættbálksnafninu með Super fyrir framan ef hermaðurinn er superhermaður

        :return: str
        """
        return '{}{}'.format('Super' if self.is_super else '', self.faction.name)

    def __str__(self):
        """
        Skilar útskrift á eiginleikum hermannsins

        :return: str
        """
        return 'Nafn = {} Líf = {} Vopn = {} Afl = {}'.format(self.name, self.hp, self.weapon_type, self.power)

    def __repr__(self):
        return self.__str__()


class Faction:
    """
    Ættbálkur. Inniheldur breytur og föll tengd ættbálkum
    """

    def __init__(self, name, number_of_soldiers, number_of_super_soldiers, user_controlled=False):
        """
        Býr til tilvik af ættbálki. Vistar eiginleika ættbálksins sem tilviksbreytur og býr til hermenn ættbálksins.

        :param name: str
        :param number_of_soldiers: int
        :param number_of_super_soldiers: int
        :param user_controlled: bool
        """
        self.name = name
        self.userControlled = user_controlled
        self.defeated = False

        self.soldiers = [Faction.generate_soldier(self, False) for i in range(number_of_soldiers)]
        self.soldiers += [Faction.generate_soldier(self, True) for i in range(number_of_super_soldiers)]

    def generate_soldier(self, is_super):
        """
        Fallið býr til hermann með tilviljanakenda eiginleika eftir því hvort hann er súperhermaður eða ekki

        :param is_super: bool
        :return: Soldier
        """
        if is_super:
            return Soldier(random.randint(10, 15), random.randint(1, 3), random.randint(4, 9), True, self)
        else:
            return Soldier(random.randint(1, 5), random.randint(1, 3), random.randint(1, 5), False, self)

    def pick_soldier(self):
        """
        Velur hermann úr ættbálkinum. Annaðhvort tilviljanakent ef honum er ekki stjórnað af notanda annars er
        notanda boðið uppá að velja hermann.

        :return: Soldier
        """
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
        """
        Fjarlægir hermann úr ættbálkinum og athugar hvort að við það hafi ættbálkurinn verið sigraðar.

        :param soldier: Soldier
        :return: None
        """
        self.soldiers.remove(soldier)
        if len(self.soldiers) == 0:
            self.defeated = True

    @property
    def number_of_soldiers(self):
        """
        Skilar fjölda venjulegra hermanna í ættbálkinum

        :return: int
        """
        return len([soldier for soldier in self.soldiers if not soldier.is_super])

    @property
    def total_hit_points_of_soldiers(self):
        """
        Skilar heildarfjölda lífa venjulegra hermanna í ættbálkinum

        :return: int
        """
        return sum([soldier.hp for soldier in self.soldiers if not soldier.is_super])

    @property
    def number_of_super_soldiers(self):
        """
        Skilar fjölda súperhermanna í ættbálkinum

        :return: int
        """
        return len([soldier for soldier in self.soldiers if soldier.is_super])

    @property
    def total_hit_points_of_super_soldiers(self):
        """
        Skilar heildarfjölda lífa súperhermanna í ættbálkinum

        :return: int
        """
        return sum([soldier.hp for soldier in self.soldiers if soldier.is_super])

    @property
    def total_army_size(self):
        """
        Skilar heildarfjölda allra hermanna í ættbálkinum

        :return: int
        """
        return len(self.soldiers)

    @property
    def total_army_hit_points(self):
        """
        Skilar heildarfjölda lífa allra hermanna í ættbálkinum

        :return: int
        """
        return sum([soldier.hp for soldier in self.soldiers])


def get_integer_from_user(prompt):
    """
    Tekur við tölu frá notanda á öruggan hátt.
    Ef það sem notandinn sló inn skilar villu þegar reynt er að breyta því í int þæa er prentuð villumelding
    og beðið aftur um tölu frá notanda þangað til að notandinn slær inn gilda tölu.

    :param prompt: str
    :return: int
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Hér þarf að slá inn tölu')
