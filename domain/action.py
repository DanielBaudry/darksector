from abc import ABC, abstractmethod

from domain.character import Character
from domain.resources import Resource, ResourceType


class Action(ABC):
    name: str
    base_energy_cost: int

    @abstractmethod
    def execute(self, character: Character, *args, **kwargs):
        pass

class ScavengeAction(Action):
    def __init__(self) -> None:
        self.name = "Scavenge"
        self.base_energy_cost = 40

    def execute(self, character: Character, *args, **kwargs):
        # get region from args
        region = args[0]

        # generate resources
        generated_resources = region.generate_resources()
        print(generated_resources)

        # add resources to character's inventory
        for res in generated_resources:
            character.add_resource_amount(res)
        
        character.remove_resource_amount(self.compute_energy_cost(character))

    def compute_energy_cost(self, character: Character) -> Resource:
        # TODO: energy cost can vary based on character's researches or skills
        return Resource(ResourceType.ENERGY, self.base_energy_cost)
