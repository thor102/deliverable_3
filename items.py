from dice import Dice


class Weapon:
    def __init__(self, name: str, damage_dice: Dice) -> None:
        self.name = name
        self.damage_dice = damage_dice 


    def roll_damage(self) -> int:
        return self.damage_dice.roll() 


sword = Weapon("sword of the morning", Dice(6))

