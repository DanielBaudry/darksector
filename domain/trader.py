from domain.base_character import BaseCharacter
from domain.character import PlayerCharacter
from domain.character_region import CharacterRegion
from domain.resources import Resource


class Trader(BaseCharacter):
    name: str
    region: CharacterRegion
    resources: list[Resource]

    def __init__(self, name: str, region: CharacterRegion, resources: list[Resource]) -> None:
        self.name = name
        self.region = region
        self.resources = resources
    
    def sell_resource_to_character(self, character: PlayerCharacter, resource: Resource) -> None:
        self.resources.remove(resource)
        character.add_resource_amount(resource)
