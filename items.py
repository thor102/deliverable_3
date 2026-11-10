from dice import Dice


class Weapon:
    """Represents a weapon using dice for damage."""
    def __init__(self, name: str, damage_dice: Dice) -> None:  
        """              
        Initialise the Weapon
        Args:
            name (str): The name of the weapon. 
            damage_dice (Dice) The Dice object used to determine weapon damage."""
        self.name = name
        self.damage_dice = damage_dice 


    def roll_damage(self) -> int:
        """Return weapon damage based on a dice roll."""
        return self.damage_dice.roll()      
