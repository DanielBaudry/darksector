from domain.dark_zone import DarkZone
from infrastructure.reward_generator_random import RewardGeneratorRandom
from domain.fight import Fight
from domain.monster import Monster
from domain.player import Player
from infrastructure.fight_logger_in_memory import FightLoggerInMemory
from infrastructure.views import display_turn_summary
from infrastructure.player_actions import get_user_action


if __name__ == '__main__':
    # ======== Get from data source ====================
    # config
    fight_logger = FightLoggerInMemory()
    reward_generator = RewardGeneratorRandom()

    player = Player('John', health=100)

    monster1 = Monster(health=20)
    monster2 = Monster(health=20)
    monster3 = Monster(health=20)
    monster4 = Monster(health=20)
    monster5 = Monster(health=20)
    monsters = [monster1, monster2]

    dark_zone = DarkZone(
        levels=[
            [monster1, monster2],
            #[monster3, monster4, monster5]
        ],
        possible_rewards=['épée', 'bouclier'],
        reward_generator=reward_generator,
    )

    while dark_zone.rewards is None:
        fight = Fight(player, dark_zone.get_current_level_monsters())
        fight.register(fight_logger)
        fight.register(dark_zone)
        # ======================================

        fight_result = True
        print('Match Start')
        display_turn_summary(fight.get_details())
        while fight.is_running:
            # route param
            user_action_monster_index = get_user_action()
            try:
                fight_result = fight.run(user_action_monster_index)
            except Exception as e:
                print(e)
            else:
                print(fight_logger.last_message())
                display_turn_summary(fight.get_details())

        print("You WIN") if fight_result else print("You LOSE")
        print("+++++++++++++++++++++++++++")
        for msg in fight_logger.messages:
            print(msg)
        print("+++++++++++++++++++++++++++")
        print('Match End')

    print(f'Vous avez gagné: {dark_zone.get_rewards()}')
