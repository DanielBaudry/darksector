from typing import List

from domain.player.experience_levels import ExperienceLevel
from domain.skill.skill import Skill

BASIC_ATTACK_ENERGY_COST = 10


class Player:
    def __init__(self, name: str,
                 identifier: int = None,
                 max_life: int = 200,
                 life: int = 200,
                 max_energy: int = 100,
                 energy: int = 100,
                 max_damage: int = 10,
                 damage: int = 10,
                 max_armor: int = 10,
                 armor: int = 10,
                 experience: int = 0,
                 skills: List[Skill] = []):
        self.identifier = identifier
        self.name = name
        self.max_life = max_life
        self.life = life
        self.max_energy = max_energy
        self.energy = energy
        self.damage = damage
        self.max_damage = max_damage
        self.armor = armor
        self.max_armor = max_armor
        self.experience = experience
        self.skills = skills

    @property
    def level(self):
        for xp in ExperienceLevel:
            if xp.value['min'] <= self.experience <= xp.value['max']:
                return xp.value['level']
        return ExperienceLevel.level_10.value['level']

    def basic_attack(self, sector_monster) -> None:
        if self.energy >= BASIC_ATTACK_ENERGY_COST and sector_monster.quantity > 0:
            sector_monster.receive_damage(self.damage)
            self.energy -= BASIC_ATTACK_ENERGY_COST

    def use_skill(self, skill: Skill, sector_monster):
        if self.energy >= skill.energy_cost:
            if sector_monster:
                sector_monster.receive_damage(skill.damage)
            self.life = int(self.life * (1 + skill.life_bonus / 100))
            self.armor = int(self.armor * (1 + skill.armor_bonus / 100))
            self.damage = int(self.damage * (1 + skill.damage_bonus / 100))
            self.energy -= skill.energy_cost

    def receive_damage(self, damage: int):
        self.life = int(max(0, self.life - damage * (1 - self.armor / 100)))

    def gain_experience(self, experience: int):
        previous_level = self.level
        self.experience += experience
        new_level = self.level
        [self.level_up() for i in range(previous_level, new_level)]

    def level_up(self):
        self.max_life = int(self.max_life * 1.10)
        self.max_damage = int(self.max_damage * 1.10)

    def is_dead(self) -> bool:
        return self.life == 0
