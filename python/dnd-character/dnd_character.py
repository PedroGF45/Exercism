from random import randint
from math import floor

def modifier(constitution):
        return floor((constitution - 10)/2) 

class Character:

    def __init__(self):
        # stats
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.constitution = self.ability()

        # hitpoints
        self.hitpoints = 10 + modifier(self.constitution)


    def ability(self):

        rolls = []

        # get random dices' values
        for i in range(4):
            rolls += [randint(0, 6)]
        
        # sort the array for ascending order
        rolls.sort()

        # delete first element
        rolls = rolls[1:]

        return sum(rolls)
