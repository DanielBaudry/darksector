from domain.sector import DarkSector, Sector
from domain.player import Player
from domain.sector_monsters import SectorMonster
from infrastructure.repository.monster.monster_in_memory_repository import MonsterInMemoryRepository


def test_darksector():
    monster_in_memory_repository = MonsterInMemoryRepository()
    darksector = DarkSector(levels=5, monster_repository=monster_in_memory_repository)
    for sector in darksector.sectors:
        print("Darksector Level: ", sector.level)
        print(sector.monsters)


def test_player():
    monster_in_memory_repository = MonsterInMemoryRepository()
    darksector = DarkSector(levels=5, monster_repository=monster_in_memory_repository)

    player1 = Player(identifier=1, name='Player1', life=200, energy=100, damage=100, armor=10)

    sector = darksector.sectors[0]
    current_monsters = sector.monsters

    for monster in current_monsters:
        print("%s: %s" % (monster.monster.name, monster.quantity))

    for monster in current_monsters:
        print("Player 1 attack")
        player1.basic_attack(monster)

    for monster in current_monsters:
        print("%s: %s" % (monster.monster.name, monster.quantity))


def test_fixed_darksector():
    monster_in_memory_repository = MonsterInMemoryRepository()
    zergling = monster_in_memory_repository.get_monster('Zergling')

    sector1 = Sector(level=1, monsters=[
        SectorMonster(level=1, monster=zergling, monster_repository=monster_in_memory_repository, quantity=10),
        SectorMonster(level=1, monster=zergling, monster_repository=monster_in_memory_repository, quantity=10)],
                     monster_repository=monster_in_memory_repository)

    sector2 = Sector(level=2, monsters=[
        SectorMonster(level=1, monster=zergling, monster_repository=monster_in_memory_repository, quantity=15)],
                     monster_repository=monster_in_memory_repository)

    darksector = DarkSector(levels=5,
                            monster_repository=monster_in_memory_repository,
                            sectors=[sector1, sector2])

    for sector in darksector.sectors:
        print("Darksector Level: ", sector.level)
        for sector_monster in sector.monsters:
            print("%s: %s" % (sector_monster.monster.name, sector_monster.quantity))


def test_donjon():
    # given
    monster_in_memory_repository = MonsterInMemoryRepository()
    darksector = DarkSector(levels=5, monster_repository=monster_in_memory_repository)

    player1 = Player(identifier=1, name='Player1', life=200, energy=100, damage=100, armor=10)

    # when
    dungeon_sector = darksector.sectors[0]
    print("Donjon niveau: ", dungeon_sector.level)
    for monster in dungeon_sector.monsters:
        print(f"%s: %s" % (monster.monster.name, monster.quantity))

    player1.basic_attack(dungeon_sector.monsters[0])  # dungeon_sector.monsters[0].receieve_damage(player_attack)
    print("Player1 attack")
    dungeon_sector.monsters[0].attack(player1)  # player1.receive_damage(monster_attack)
    print("Monster1 attack")
    print("Player1 life: ", player1.life)

    for monster in dungeon_sector.monsters:
        print(f"%s: %s" % (monster.monster.name, monster.quantity))

    player1.basic_attack(dungeon_sector.monsters[0])  # dungeon_sector.monsters[0].receieve_damage(player_attack)
    # raise SectorClear

    player1.gain_experience(dungeon_sector.rewards())
    print("Player XP: ", player1.experience)
    print("Player level: ", player1.level)


if __name__ == "__main__":
    print("==================================")
    test_darksector()
    print("==================================")
    test_player()
    print("==================================")
    test_donjon()
    print("==================================")
    test_fixed_darksector()
