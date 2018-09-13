import random

name = "main";

class Ability:

    name = "";
    attack_strength = 0;

    def __init__(self, name, attack_strength):
        self.name = name;
        self.attack_strength = attack_strength;
        print("example");

    def attack(self):
        # Return attack value
        print("example");

    def update_attack(self, attack_strength):
            # Update attack value
        print("example");
class Hero:

    name = ""
    abilities = Ability();

    def __init__(self, name): # Initialize starting values
        self.name = name;
        self.abilities = list()
    def add_ability(self, ability): # Add ability to abilities list
        abilities.append(ability);
        print("example");

    def attack(self): # Run attack() on every ability hero has
        for ability in abilities:
            ability.attack();
        print("example");


if name == "main":
    hero = Hero("Wonder Woman")
    # print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
