import random 


class Dice:
    """Represents a dice to make it more random what happens."""
    def __init__(self, sides: int = 6) -> None:
        """       
        Initialise the Dice
        Args:
            sides (int): The amount of sides on the dice (default 6)."""
        self.sides= max(sides, 2)


    def roll(self) -> int:
        """returns random value from 1 to 6 or the value the user sets."""
        return random.randint(1, self.sides)


    def __repr__(self) -> str:
        """Return a string representation of the Dice object."""
        return f"Dice(sides={self.sides})"     


    def __call__(self) -> int:
        """Allow the Dice object to be called directly to roll the dice."""
        return self.roll()
