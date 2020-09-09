from enum import Enum


class InMemorySkills(Enum):
    grenade = {
        'name': 'Plasma grenade',
        'damage': 80,
        'energy_cost': 30,
        'armor_bonus': 0,
        'damage_bonus': 0,
        'life_bonus': 0,
    }

    blast = {
        'name': 'Blast',
        'damage': 40,
        'energy_cost': 20,
        'armor_bonus': 0,
        'damage_bonus': 0,
        'life_bonus': 0,
    }

    force_shield = {
        'name': 'Force Shield',
        'damage': 0,
        'energy_cost': 30,
        'armor_bonus': 25,
        'damage_bonus': 0,
        'life_bonus': 0,
    }

    steroids = {
        'name': 'Steroids',
        'damage': 0,
        'energy_cost': 25,
        'armor_bonus': 0,
        'damage_bonus': 25,
        'life_bonus': 0,
    }

    painkiller = {
        'name': 'Painkiller',
        'damage': 0,
        'energy_cost': 20,
        'armor_bonus': 0,
        'damage_bonus': 0,
        'life_bonus': 20,
    }
