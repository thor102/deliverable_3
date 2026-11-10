class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100).
            damage (int): 	Damage dealt when the character attacks (default = 10).
            weapon (Weapon): Optional weapon equipped by the character (default = None).
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon
        
    def attack(self, target) -> None:
        """Attack and give damage value to target character."""
        if self.weapon is not None:
            damage_done = self.weapon.roll_damage()
        else:
            damage_done = self.damage
        target.take_damage(damage_done)


    def take_damage(self, damage_done: int) -> None:
        """Takes damage from attack and takes it from hp amount."""
        self._hp -= abs(damage_done)
        self._hp = max(self._hp, 0)  # Target hp cannot end up lower than 0


    def heal(self, healing: int = 20) -> None:
        """Restore HP without exceeding the maximum HP."""
        self._hp += abs(healing) # abs makes sure that user can't use negtaive values.
        self._hp = min(self.hp_max, self._hp)

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    
    @property 
    def is_alive(self) -> bool:
        """Check whether the character is still alive."""
        if self.hp > 0:
            return True 
        else:
            return False 


class Warrior(Character):
    """A heavily armored character."""

    def __init__(
        self,
        name: str,
        hp_max: int = 120, 
        damage: int = 15,  
        armor: int = 5,
        weapon=None
    ) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, damage_done: int) -> None:
        """Reduce incoming damage by armor."""
        actual_damage = max(damage_done - self.armor, 0)
        self._hp -= actual_damage
        self._hp = max(self._hp, 0)

    def __str__(self) -> str:
        return (
            f"Warrior: {self.name}, HP={self.hp}, "
            f"Damage={self.damage}, Armor={self.armor}"
        )

class Mage(Character):
    """A magic user with mana."""

    def __init__(
        self, 
        name: str, 
        hp_max: int = 80, 
        damage: int = 10, 
        mana: int = 50,
        spell_damage: int = 25,
        weapon=None,
    )-> None:
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.spell_damage = spell_damage

    def attack(self, target) -> None:
        """
        Uses a spell if enough mana is available.
        Otherwise performs a normal attack.
        """

        if self.mana >= 10:
            self.mana -=10
            target.take_damage(self.spell_damage)

        elif self.weapon is not None:
            target.take_damage(self.weapon.roll_damage())

        else:
            target.take_damage(self.damage)

    def __str__(self) -> str:
        return (
            f"Mage: {self.name}, HP={self.hp}, "
            f"Damage={self.damage}, Mana={self.name}"
        )
