from enum import Enum

from domain.gear.gear import GearQuality, PlayerPart


class InMemoryGears(Enum):
    rifle1 = {
        'id': 'rifle1',
        'name': 'Rifle RXC-4',
        'quality': GearQuality.normal,
        'credit_cost': 1200,
        'level_requirement': 1,
        'player_part': PlayerPart.both_hands,
        'damage': 40,
        'life': 0,
        'armor': 0,
        'energy': 0,
    }

    chest_armor1 = {
        'id': 'chest_armor1',
        'name': 'Exo Suit TX',
        'quality': GearQuality.rare,
        'credit_cost': 2400,
        'level_requirement': 2,
        'player_part': PlayerPart.chest,
        'damage': 0,
        'life': 200,
        'armor': 10,
        'energy': 10,
    }
