from typing import List, Optional

from domain.gear.gear import Gear, PlayerPart, Weapon, Armor
from domain.player.experience_levels import ExperienceLevel
from domain.player.player_gear import PlayerGear
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
                 credits_amount: int = 0,
                 skills: List[Skill] = [],
                 gears: List[PlayerGear] = []):
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
        self.credits = credits_amount
        self.experience = experience
        self.skills = skills
        self.gears = gears

    @property
    def head(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.head:
                return player_gear.gear
        return None

    @property
    def chest(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.chest:
                return player_gear.gear
        return None

    @property
    def legs(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.legs:
                return player_gear.gear
        return None

    @property
    def feet(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.feet:
                return player_gear.gear
        return None

    @property
    def left_shoulder(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.left_shoulder:
                return player_gear.gear
        return None

    @property
    def right_shoulder(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.right_shoulder:
                return player_gear.gear
        return None

    @property
    def left_hand(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped \
                    and (player_gear.gear.player_part == PlayerPart.left_hand
                         or player_gear.gear.player_part == PlayerPart.both_hands):
                return player_gear.gear
        return None

    @property
    def right_hand(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped \
                    and (player_gear.gear.player_part == PlayerPart.right_hand
                         or player_gear.gear.player_part == PlayerPart.both_hands):
                return player_gear.gear
        return None

    @property
    def left_arm(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.left_arm:
                return player_gear.gear
        return None

    @property
    def right_arm(self) -> Optional[Gear]:
        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == PlayerPart.right_arm:
                return player_gear.gear
        return None

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

    def gain_credits(self, credits_amount: int):
        self.credits += credits_amount

    def level_up(self):
        self.max_life = int(self.max_life * 1.10)
        self.max_damage = int(self.max_damage * 1.10)

    def is_dead(self) -> bool:
        return self.life == 0

    def receive_gear(self, gear: Gear):
        self.gears.append(
            PlayerGear(
                gear=gear,
            )
        )

    def equip_player_gear(self, player_gear_id: int, to_equip: bool):
        expected_gear = next(iter([player_gear for player_gear in self.gears
                                   if player_gear.identifier == player_gear_id]), None)

        for player_gear in self.gears:
            if player_gear.is_equipped and player_gear.gear.player_part == expected_gear.gear.player_part:
                player_gear.is_equipped = False
                self.unequip_gear(gear=player_gear.gear)

        expected_gear.is_equipped = to_equip
        gear = expected_gear.gear
        if to_equip is True:
            self.equip_gear(gear=gear)
        else:
            self.unequip_gear(gear=gear)

    def equip_gear(self, gear: Gear):
        if isinstance(gear, Weapon):
            self.max_damage += gear.damage
            self.max_energy += gear.energy
            self.damage = self.max_damage
            self.energy = self.max_energy
        elif isinstance(gear, Armor):
            self.max_life += gear.life
            self.max_armor += gear.armor
            self.max_energy += gear.energy
            self.life = self.max_life
            self.armor = self.max_armor
            self.energy = self.max_energy

    def unequip_gear(self, gear: Gear):
        if isinstance(gear, Weapon):
            self.max_damage -= gear.damage
            self.max_energy -= gear.energy
            self.damage = self.max_damage
            self.energy = self.max_energy
        elif isinstance(gear, Armor):
            self.max_life -= gear.life
            self.max_armor -= gear.armor
            self.max_energy -= gear.energy
            self.life = self.max_life
            self.armor = self.max_armor
            self.energy = self.max_energy
