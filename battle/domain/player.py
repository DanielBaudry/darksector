from typing import List, Optional

from domain.fighter import Fighter, FighterAbility


class Player(Fighter):
    def __init__(self, name: str, health: int, damage: int = 10,
                 additional_abilities: Optional[List[FighterAbility]] = None):
        super().__init__(health, damage)
        self.name = name
        if additional_abilities:
            self.abilities += additional_abilities
