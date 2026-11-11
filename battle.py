from character import Character


class Battle:
    """Manage turn-based combat between two characters."""

    def __init__(
        self,
        hero: Character,
        enemy: Character,
        max_rounds: int = 100,
    ) -> None:
        """
        Initialise the Battle.

        Args:
            hero (Character): Attacks first each round.
            enemy (Character): Attacks back if still alive.
            max_rounds (int): Safety limit to avoid infinite battles (default = 100).
        """
        self.hero = hero
        self.enemy = enemy
        self.max_rounds = max_rounds

    def play_round(self) -> None:
        """Hero attacks enemy; if enemy is still alive, enemy attacks hero."""
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> Character | None:
        """
        Play rounds until one character dies or max_rounds is reached.

        Returns:
            Character | None: The winner, or None if nobody won.
        """
        round_number = 1

        while self.hero.is_alive and self.enemy.is_alive:
            if round_number > self.max_rounds:
                print(f"\nNo winner after {self.max_rounds} rounds")
                return None

            print(f"\n--- Round {round_number} ---")
            self.play_round()
            print(f"{self.hero.name}: {self.hero.hp}/{self.hero.hp_max} HP")
            print(f"{self.enemy.name}: {self.enemy.hp}/{self.enemy.hp_max} HP")
            round_number += 1

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"\nWinner: {winner.name}")
        return winner