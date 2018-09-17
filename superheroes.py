import random


class Ability:

    name = ""
    attack_strength = 0

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

class Hero:

    # name = ""
    # abilities = list();

    def __init__(self, name): # Initialize starting values
        self.name = name
        self.abilities = list()
    def add_ability(self, ability): # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self): # Run attack() on every ability hero has
        total = 0

        for ability in self.abilities:
            total += ability.attack()

        return total


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    # print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
