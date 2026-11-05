from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, healing: int = 20, weapon = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.healing = healing
        self.weapon = weapon
        
    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            damage_done = self.weapon.roll_damage()
        else:
            damage_done = self.damage
        target.take_damage(damage_done)



    def take_damage(self, damage_done) -> None:
        """ """
        self._hp -= damage_done
        self._hp = max(self._hp, 0)  # Target hp cannot end up lower than 0


    def heal(self, healing) -> None:
        """ """
        self._hp += healing
        self._hp = min(self.hp_max, self._hp)

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    
    @property 
    def is_alive(self) -> bool:
        """ """
        if self.hp > 0:
            return True 
        else:
            return False 


class Warrior(Character):
    """ """
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, healing: int = 20, weapon = None, armor: int = 5) -> None:
        super().__init__(name, hp_max, damage, healing, weapon)
        self.armor = armor 

    def take_damage(self, damage_done) -> None:
        """ """
        self.armor = max(self.armor, 0)
        blocked = damage_done - self.armor
        super().take_damage(blocked)

    


