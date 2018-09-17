from io import BytesIO
import random

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
            total_defense += x.defend
        if self.health < 1:
            total_defense = 0

    #subtract the damage amount from the hero's health. Update death count if hero dies
    def take_damage(self, damage_amt):
        self.health -= damage_amt
        if self.health < 1:
            self.deaths += 1

    def add_kill(self, num_kills): #add the number of kills to self.kills
        self.kills += num_kills

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

class Armor:
    def __init__(self, name, defense): #Instantiate name and defense strength
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
