from enum import Enum


class InMemoryMonsters(Enum):
    zergling = {
        'name': 'Zergling',
        'life': 20,
        'damage': 5,
        'armor': 0,
        'experience_gain': 1,
    }

    hydralisk = {
        'name': 'Hydralisk',
        'life': 45,
        'damage': 12,
        'armor': 5,
        'experience_gain': 2,
    }
