import random

name = "main";

class Hero:

    name = ""

    def __init__(self, name): # Initialize starting values
        self.name = name;
    def add_ability(self, ability):        # Add ability to abilities list

        print("example");

    def attack(self):          # Run attack() on every ability hero has

        print("example");

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


if name == "main":
    # If you run this file from the terminal this block is executed.
    my_hero = Hero("bob");
    print(my_hero.name);
    my_hero.add_ability;
    my_hero.attack;
