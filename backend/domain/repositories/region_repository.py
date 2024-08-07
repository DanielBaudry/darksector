from domain.character import PlayerCharacter
from domain.city import City


class RegionRepository:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def get_character_city(self, character: PlayerCharacter) -> City:
        # TODO: connect to database and retrieve city from character's id
        pass