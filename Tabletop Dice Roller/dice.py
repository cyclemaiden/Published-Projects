import random

# A die object that can be rolled.
class Die:
    def __init__(self, numberOfSides, color="no color"):
        # self.name = name
        self.sides = numberOfSides
        self.color = color

    def roll(self):
        x = random.randint(1, self.sides)
        return(x)


# Allows for multiple dice to exist in one object so they can all be rolled at once.
class MultiDice:
    def __init__(self, die, quantity):
        self.die = die
        self.quantity = quantity

    def roll(self):
        rollList = []
        for i in range(self.quantity):
            r = self.die.roll()
            rollList.append(r)
        total = sum(rollList)
        comboName = str(self.quantity)+"d"+str(self.die.sides)
        return(total, comboName, rollList)

# List of Common Dice
'''
d4 = Die("d4", 4)
d6 = Die("d6", 6)
d8 = Die("d8", 8)
d10 = Die("d10", 10)
d12 = Die("d12", 12)
d20 = Die("d20", 20)
d100 = Die("d100", 100)
'''

'''
x = d100.roll()

print(x)

print(d100.color)



testdie = Die("d100", 100)

testdicelist = DiceList(testdie, 4)

x,y, z = testdicelist.roll()

print(x)
print(y)
print(z)
'''

