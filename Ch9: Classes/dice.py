from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides


    def roll_die(self):
        """Prints a random number between 1 and the number of sides the die has."""
        print(f"A {randint(1,self.sides)} was rolled!")

new_die6 = Dice()
new_die6.roll_die()

new_die10 = Dice(10)
new_die10.roll_die()

new_die20 = Dice(20)
new_die20.roll_die()