from domain.experience_levels import ExperienceLevel


class Player:
    def __init__(self, name: str, identifier: int = None, life: int = 200, energy: int = 100, damage: int = 10,
                 armor: int = 10,
                 experience: int = 0):
        self.identifier = identifier
        self.name = name
        self.life = life
        self.energy = energy
        self.damage = damage
        self.armor = armor
        self.experience = experience

    @property
    def level(self):
        for xp in ExperienceLevel:
            if xp.value['min'] <= self.experience <= xp.value['max']:
                return xp.value['level']
        return ExperienceLevel.level_10.value['level']

    def basic_attack(self, sector_monster) -> None:
        sector_monster.receive_damage(self.damage)

    def receive_damage(self, damage: int):
        self.life = int(max(0, self.life - damage * (1 - self.armor / 100)))

    def gain_experience(self, experience: int):
        self.experience += experience

    def is_dead(self) -> bool:
        return self.life == 0
