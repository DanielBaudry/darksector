from domain.base_character import BaseCharacter
from domain.character import PlayerCharacter
from domain.resources import Resource


class Trader(BaseCharacter):
    def sell_resource_to_character(self, character: PlayerCharacter, resource: Resource) -> None:
        self.resources.remove(resource)
        character.add_resource_amount(resource)

    def resource_provisioning(self):
        # TODO: implement resource provisioning logic
        pass
