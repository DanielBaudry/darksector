from domain.ability import AllAbilities
from domain.fight import Fight


def run_dark_zone(player, dark_zone, fight_logger, display_turn_summary, get_user_action) -> bool:
    while dark_zone.rewards is None:
        fight = Fight(player, dark_zone.get_current_level_monsters())
        fight.register(fight_logger)
        fight.register(dark_zone)
        # ======================================

        fight_result = True
        last_log_id = len(fight_logger.messages)

        display_turn_summary(fight.get_details())
        while fight.is_running:
            # route param
            user_action_monster_index, ability = get_user_action()
            # remove from here
            if ability == 'g':
                user_ability = AllAbilities.GRENADE
            elif ability == 's':
                user_ability = AllAbilities.STIMULANT

            else:
                user_ability = AllAbilities.BASIC_ABILITY

            try:
                fight_result = fight.run(user_action_monster_index, user_ability)
            except Exception as e:
                print(e)
            else:
                for msg in fight_logger.get_messages_from(last_log_id):
                    print(msg)
                last_log_id = len(fight_logger.messages)
                display_turn_summary(fight.get_details())

    return fight_result
