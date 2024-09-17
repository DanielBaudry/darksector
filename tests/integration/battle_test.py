from domain.ability import AllAbilities
from domain.fight import Fight
from domain.monster import Monster
from domain.player import Player


class BattleTest:
    class WithBasicAbilityTest:
        def test_one_to_one_battle_with_player_win(self):
            # given
            player = Player('John', health=100, damage=10)
            monster = Monster(health=20, damage=10)
            fight = Fight(player, [monster])

            fight_result = None
            turn_count = 0

            # when
            while fight_result is None:
                fight_result = fight.run(monster_index=0)
                turn_count += 1

            # then
            assert fight_result is True
            assert turn_count == 2

        def test_one_to_one_battle_with_player_lose(self):
            # given
            player = Player('John', health=10, damage=10)
            monster = Monster(health=20, damage=10)
            fight = Fight(player, [monster])

            fight_result = None
            turn_count = 0

            # when
            while fight_result is None:
                fight_result = fight.run(monster_index=0)
                turn_count += 1

            # then
            assert fight_result is False
            assert turn_count == 1

        def test_multiple_monsters_battle_with_player_win(self):
            # given
            player = Player('John', health=100, damage=10)
            monsters = [Monster(health=20, damage=5), Monster(health=30, damage=5), Monster(health=20, damage=5)]
            fight = Fight(player, monsters)

            # mock fight is running
            fight_result = None
            turn_count = 0
            # mock user behavior
            monster_index_to_attack = 0

            # when
            while fight_result is None:
                if monsters[monster_index_to_attack].health == 0:
                    monster_index_to_attack += 1
                fight_result = fight.run(monster_index=monster_index_to_attack)
                turn_count += 1

            # then
            assert fight_result is True
            assert turn_count == 7

    class WithAllAbilitiesTest:
        def test_multiple_monsters_battle_with_player_win(self):
            # given
            player = Player('John', health=100, damage=10)
            monsters = [Monster(health=20, damage=5), Monster(health=30, damage=5), Monster(health=20, damage=5)]
            fight = Fight(player, monsters)

            # mock fight is running
            fight_result = None
            turn_count = 0
            # mock user behavior
            monster_index_to_attack = 0
            ability = AllAbilities.GRENADE

            # when
            while fight_result is None:
                if monsters[monster_index_to_attack].health == 0:
                    monster_index_to_attack += 1
                try:
                    fight_result = fight.run(monster_index=monster_index_to_attack, player_ability=ability)
                    turn_count += 1
                except Exception:
                    ability = AllAbilities.BASIC_ABILITY

            # then
            assert fight_result is True
            assert turn_count == 6
