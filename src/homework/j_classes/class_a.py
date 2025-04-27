import random

class die:

    def __init__(self):
        """ Initialize the roll history """
        self.roll_history = []

    def __str__(self):
        return f"Last roll: {self.roll_history[-1]}"

    def roll(self):
        value = random.randint(1,6)
        self.roll_history.append(value)
        return value
