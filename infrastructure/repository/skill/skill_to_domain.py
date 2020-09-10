from domain.skill.skill import Skill
from infrastructure.repository.skill.in_memory_skills import InMemorySkills


def to_domain(in_memory_skill: InMemorySkills) -> Skill:
    return Skill(
        identifier=in_memory_skill['id'],
        name=in_memory_skill['name'],
        damage=in_memory_skill['damage'],
        energy_cost=in_memory_skill['energy_cost'],
        armor_bonus=in_memory_skill['armor_bonus'],
        damage_bonus=in_memory_skill['damage_bonus'],
        life_bonus=in_memory_skill['life_bonus'],
    )
