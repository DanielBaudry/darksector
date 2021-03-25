from typing import Dict


def display_turn_summary(fight_details: Dict):
    fight_turn = fight_details.get('fight_turn')
    player = fight_details.get('player')
    monsters = fight_details.get('monsters')
    print("====================")
    print(f"======Tour {fight_turn}========")
    print("====================")
    print(f'Player: {player.health}')
    for index, m in enumerate(monsters):
        print(f'Monster {index + 1}: {m.health}')
    print("====================")