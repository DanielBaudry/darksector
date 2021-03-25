from random import randrange

from domain.dark_zone import DarkZone
from domain.monster import Monster
from domain.player import Player
from run_dark_zone import run_dark_zone
from infrastructure.fight_logger_in_memory import FightLoggerInMemory
from infrastructure.player_actions import get_menu_action, get_user_action
from infrastructure.reward_generator_random import RewardGeneratorRandom
from infrastructure.views import display_turn_summary

if __name__ == '__main__':
    # ======== Get from data source ====================
    # config
    fight_logger = FightLoggerInMemory()
    reward_generator = RewardGeneratorRandom()

    player = Player('John', health=100)

    game_is_running = True
    while game_is_running:
        menu_action = get_menu_action()
        if menu_action == 'd':
            dark_zone = DarkZone(
                levels=[
                    [Monster(health=randrange(10, 20)), Monster(health=randrange(10, 20)),
                     Monster(health=randrange(10, 20))],
                    [Monster(health=randrange(20, 30)), Monster(health=randrange(20, 30))]
                ],
                possible_rewards=['Fusil x23', 'Casque ZE'],
                reward_generator=reward_generator,
            )

            print("+++++++++++++++++++++++++++")
            print('Match Start')
            fight_result = run_dark_zone(player, dark_zone, fight_logger, display_turn_summary, get_user_action)
            print("You WIN") if fight_result else print("You LOSE")
            print('Match End')
            print("+++++++++++++++++++++++++++")

            print(f'Vous avez gagné: {dark_zone.get_rewards()}')

            # reset player after dark zone
            player.health = 100
        else:
            print("Action incorrecte")
    print("Bye")
