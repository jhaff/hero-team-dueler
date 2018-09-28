from io import BytesIO
import random
from termcolor import colored

class Ability:

    name = ""
    attack_strength = 0    # represents the maximum attack strength.


    def __init__(self, name, attack_strength): # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength

    #  generate and return attack value of the ability
    def attack(self):

        lower_value = self.attack_strength // 2

        return random.randint(lower_value, self.attack_strength)


    # update the value of the current attack strength with the new value.
    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength;

#subclass of Ability
class Weapon(Ability):

    def attack(self):

    #weapons less effective than Abilities, so range from 0 to attack strength.
        return random.randint(0, self.attack_strength)


class Hero:

    def __init__(self, name, health=100): # Initialize starting values
        self.name = name
        self.abilities = list()

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability): # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self): # Run attack() on every ability hero has
        total_strength = 0
        for ability in self.abilities:
            total_strength += ability.attack()
        return total_strength


    def defend(self): #runs defend method on each armor, calculate total defense. Check if hero is dead

        total_defense = 0
        for x in self.armors:
            total_defense += x.defend()
        if self.health < 1:
            total_defense = 0
        return total_defense

    #subtract the damage amount from the hero's health. Update death count if hero dies
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        # print(self.health)
        if self.health < 1:
            self.deaths += 1

    def add_kill(self, num_kills): #add the number of kills to self.kills
        self.kills += num_kills

    def add_armor(self, armor):
        self.armors.append(armor)

class Team:
    #Instantiate resources.
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    #find and remove specified hero, or return 0 if not found
    def remove_hero(self, name):
        if self.heroes == []:
            return 0
        for x in self.heroes:
            if x.name == name:
                self.heroes.remove(x)
                return "success"
        return 0

    #loop through heroes to find a specified hero, or return 0 if not found
    def find_hero(self, name):
        for x in self.heroes:
            if x.name == name:
                return x
        return 0

    def view_all_heroes(self):
        for x in self.heroes:
            print(x.name)


    def update_kills(self, num): #updates all heroes’ in a team kill count with specified number
        for x in self.heroes:
            x.kills += num

    # Divide the total damage amongst all heroes.
    # Return the number of heros that died in attack.
    def deal_damage(self, damage):
        damage_each = damage / len(self.heroes)
        local_death_count = 0

        for x in self.heroes:
            x.take_damage(damage_each)
            if x.health < 1:
                local_death_count += 1

        return local_death_count

    def attack(self, other_team):
        total_team_attack = 0
        for x in self.heroes:
            if x.health > 0:
                total_team_attack += x.attack()

        print("Team %s attacked Team %s with an attack of %s!" % (colored(self.name, "yellow"), colored(other_team.name, "yellow"), colored(str(total_team_attack), "yellow")))


        self.update_kills(other_team.defend(total_team_attack))


    def defend(self, damage_amt): # calculate our team's total defense.

        total_team_defense = 0

        for x in self.heroes:
            total_team_defense += x.defend()

        if damage_amt > total_team_defense:
            return self.deal_damage(damage_amt - total_team_defense)

        else:
            return 0


    #resets all heroes to full health
    def revive_heroes(self, health=100):
        for x in self.heroes:
            x.health = 100

    # print the ratio of kills/deaths for each member of the team to the screen.
    def stats(self):
        for x in self.heroes:
            if x.deaths != 0:
                print(" {}'s Kill/Death Ratio: {}".format(x.name,(x.kills / x.deaths)))
            else:
                print(" {} Has only kills {}".format(x.name,(x.kills)))

    def find_health(self):
        total_health = 0
        # print("find_health %s" % (self.heroes))
        for x in self.heroes:
            print("Team: {} Hero: {} health: {}".format(self.name, x.name, x.health))
            total_health += x.health

        return total_health


class Armor:
    def __init__(self, name, defense): #Instantiate name and defense strength
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    #user to builds teams
    def build_team_one(self):
        team_name = input("What is the first team's name?")
        self.team_one = Team(team_name)
        flag = input("Add a hero? Y/N")

        if flag.upper() == "N" and len(self.team_one.heroes) == 0:
            print("There must be at least one hero in the team to begin.")
            self.build_team_one()

        while flag.upper() != "N":
            team_hero = self.build_hero()
            self.team_one.add_hero(team_hero)
            flag = input("Add an additional hero? Y/N")

        return self.team_one

    def build_team_two(self):
        team_name = input("What is the second team's name?")
        self.team_two = Team(team_name)
        flag = input("Add a hero? Y/N")

        if flag.upper() == "N" and len(self.team_two.heroes) == 0:
            print("There must be at least one hero in the team to begin.")
            self.build_team_two()

        while flag.upper() != "N":
            team_hero = self.build_hero()
            self.team_two.add_hero(team_hero)
            flag = input("Add an additional hero? Y/N")

        return self.team_two


        # Function that lets the user create a hero along with armors and abilities
    def build_hero(self):
        try:
            hero_name = input("What is this hero's name? ")

            self.hero = Hero(hero_name, 100)

            ability_count = input("How many abilities does this hero have?(Numerical input) ")
            self.create_abilities(int(ability_count))

            armor_count = input("How many pieces of armor does this hero have?(Numerical input) ")
            self.create_armors(int(armor_count))

            return self.hero

        except ValueError:
            print("You didn't enter a numerical value!")

        except KeyboardInterrupt:
            print("You tried to interrupt the program!")

   # creating abilities for hero builder
    def create_abilities(self, abilities_num):
        for ability in range(0, abilities_num):
            ability_name = input("What is the name of this ability? ")
            ability_strength = int(input("How strong is this ability? \nEnter a number: "))
            self.hero.add_ability(Ability(ability_name, ability_strength))

    # creating armors for hero builder
    def create_armors(self, armor_num):
        for armor in range(0, armor_num):
            armor_name = input("What is the name of the gear? ")
            armor_value = int(input("What is the defense value?\nEnter a number: "))
            self.hero.add_armor(Armor(armor_name, armor_value))


    #print out the battle statistics including each heroes kill/death ratio.
    def show_stats(self):

        self.team_one.stats()
        self.team_two.stats()

    def team_battle(self):
        team_one_died = 0
        team_two_died = 0
        while self.team_one.find_health() > 0 and self.team_two.find_health() > 0:
            self.team_one.attack(self.team_two)
            self.team_two.attack(self.team_one)

    def run(self):
        self.build_team_one()
        self.build_team_two()
        self.team_battle()
        self.show_stats()

if __name__ == "__main__":

    arena = Arena() # initialize arena
    arena.run()
