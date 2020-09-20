from src.domain.monster.monster import Monster
from src.domain.player.player import Player
from src.domain.sector_monsters.sector_monsters import SectorMonster
from src.domain.skill import Skill


def create_test_player():
    return Player(
        name='Player1',
        identifier=1,
        max_life=200,
        life=200,
        max_energy=200,
        energy=200,
        max_damage=20,
        damage=20,
        max_armor=10,
        armor=10,
        experience=0,
        skills=[],
    )


def create_sector_monster():
    monster = Monster(
        name='Monster1',
        damage=10,
        experience_gain=10,
        armor=0,
        life=10,
    )
    return SectorMonster(
        monster=monster,
        initial_quantity=10,
        quantity=10
    )


def create_skill(armor_bonus=20, damage=40, damage_bonus=20, life_bonus=20, energy_cost=10):
    return Skill(
        identifier='boost',
        name='Boost',
        armor_bonus=armor_bonus,
        damage=damage,
        damage_bonus=damage_bonus,
        life_bonus=life_bonus,
        energy_cost=energy_cost,
    )


class PlayerTest:
    class LevelTest:
        def should_return_1_when_player_has_no_xp(self):
            player = create_test_player()
            assert player.level == 1

        def should_return_matching_level(self):
            player = create_test_player()
            player.experience = 200
            assert player.level == 3

        def should_return_1_when_player_has_more_than_52000_xp(self):
            player = create_test_player()
            player.experience = 54000
            assert player.level == 10

    class BasicAttackTest:
        def should_do_nothing_when_sector_monster_are_no_more(self):
            player = create_test_player()
            sector_monster = create_sector_monster()
            sector_monster.quantity = 0
            player.basic_attack(sector_monster)

            assert sector_monster.quantity == 0

        def should_reduce_sector_monster_quantity_based_on_player_damage(self):
            player = create_test_player()
            player.damage = 30
            sector_monster = create_sector_monster()
            sector_monster.quantity = 10
            player.basic_attack(sector_monster)

            assert sector_monster.quantity == 7

    class ReceiveDamageTest:
        def should_decrease_player_life_of_specified_amount_when_no_armor(self):
            player = create_test_player()
            player.life = 180
            player.armor = 0
            player.receive_damage(20)

            assert player.life == 160

        def should_decrease_player_life_of_specified_amount_minus_armor_reduction(self):
            player = create_test_player()
            player.life = 180
            player.armor = 50
            player.receive_damage(20)

            assert player.life == 170

    class GainExperienceTest:
        def should_add_experience_to_player(self):
            player = create_test_player()
            player.experience = 20
            player.gain_experience(10)
            assert player.experience == 30

        def should_level_up_player_when_experience_reach_next_level(self):
            player = create_test_player()
            player.max_life = 100
            player.max_damage = 20
            player.experience = 20
            player.gain_experience(100)
            assert player.experience == 120
            assert player.max_life == 110
            assert player.max_damage == 22

    class UseSkillTest:
        def should_do_nothing_when_player_has_not_enough_energy(self):
            player = create_test_player()
            player.energy = 0
            skill = create_skill()
            skill.energy_cost = 50
            player.use_skill(skill, sector_monster=None)

            assert player.energy == 0
            assert player.life == 200
            assert player.armor == 10
            assert player.damage == 20

        def should_increase_player_stats_when_used_self_skilled(self):
            player = create_test_player()
            player.life = 100
            player.energy = 100
            skill = create_skill()
            skill.damage = 0
            skill.life_bonus = 10
            skill.energy_cost = 50
            player.use_skill(skill, sector_monster=None)

            assert player.energy == 50
            assert player.life == 110

        def should_damage_targeted_sector_monster(self):
            player = create_test_player()
            player.energy = 50
            skill = create_skill()
            skill.energy_cost = 50
            skill.damage = 50
            sector_monster = create_sector_monster()
            sector_monster.quantity = 20
            player.use_skill(skill, sector_monster=sector_monster)

            assert sector_monster.quantity == 15
