from abc import ABC
from enum import Enum


class GearQuality(Enum):
    normal = 'Normal'
    rare = 'Rare'
    unique = 'Unique'
    legendary = 'Legendary'


class PlayerPart(Enum):
    head = 'Head'
    right_shoulder = 'Right Shoulder'
    left_shoulder = 'Left Shoulder'
    chest = 'Chest'
    right_arm = 'Right Arm'
    left_arm = 'Left Arm'
    right_hand = 'Right Hand'
    left_hand = 'Left Hand'
    both_hands = 'Both Hands'
    legs = 'Legs'
    feet = 'Feet'


class Gear(ABC):
    def __init__(self,
                 identifier: str,
                 name: str,
                 quality: GearQuality,
                 credit_cost: int,
                 level_requirement: int,
                 player_part: PlayerPart):
        self.identifier = identifier
        self.name = name
        self.quality = quality
        self.credit_cost = credit_cost
        self.level_requirement = level_requirement
        self.player_part = player_part


class Weapon(Gear):
    def __init__(self, damage, energy, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage
        self.energy = energy


class Armor(Gear):
    def __init__(self, life, armor, energy, **kwargs):
        super().__init__(**kwargs)
        self.life = life
        self.armor = armor
        self.energy = energy


class Equipment(Gear):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
