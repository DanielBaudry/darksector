from src.domain.monster.monster import Monster
from src.infrastructure.repository.monster.in_memory_monsters import InMemoryMonsters


def to_domain(in_memory_monster: InMemoryMonsters) -> Monster:
    return Monster(
        name=in_memory_monster['name'],
        life=in_memory_monster['life'],
        armor=in_memory_monster['armor'],
        damage=in_memory_monster['damage'],
        experience_gain=in_memory_monster['experience_gain'],
    )
