from src.domain.gear.gear import Gear, Weapon, Armor
from src.infrastructure.repository.gear.in_memory_gear import InMemoryGears


def to_domain(in_memory_gear: InMemoryGears) -> Gear:
    if in_memory_gear['damage'] > 0:
        return Weapon(
            identifier=in_memory_gear['id'],
            name=in_memory_gear['name'],
            quality=in_memory_gear['quality'],
            credit_cost=in_memory_gear['credit_cost'],
            level_requirement=in_memory_gear['level_requirement'],
            player_part=in_memory_gear['player_part'],
            damage=in_memory_gear['damage'],
            energy=in_memory_gear['energy'],
        )
    elif in_memory_gear['life'] > 0:
        return Armor(
            identifier=in_memory_gear['id'],
            name=in_memory_gear['name'],
            quality=in_memory_gear['quality'],
            credit_cost=in_memory_gear['credit_cost'],
            level_requirement=in_memory_gear['level_requirement'],
            player_part=in_memory_gear['player_part'],
            life=in_memory_gear['life'],
            armor=in_memory_gear['armor'],
            energy=in_memory_gear['energy'],
        )
