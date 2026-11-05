import random 


class Dice:
    def __init__(self, sides=6) -> None:
        self.sides= max(sides, 2)


    def roll(self) -> int:
        return random.randint(1, self.sides)


    def __repr__(self) -> str:
        return f"Dice(sides={self.sides})"     


    def __call__(self):
        self.roll()        


d20 = Dice(sides=20)
print(d20)