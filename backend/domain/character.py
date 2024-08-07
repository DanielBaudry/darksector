from typing import Optional
from domain.base_character import BaseCharacter
from domain.resources import Resource, ResourceType


class PlayerCharacter(BaseCharacter):
    consumptions: list[Resource]
    generation: list[Resource]

    def __init__(self, name: str, consumptions: list[Resource], generation: list[Resource], resources: list[Resource], current_region: Optional["Region"] = None,  cities: Optional[list["City"]] = None) -> None:
        super().__init__(name, resources, current_region, cities)
        self.consumptions = consumptions
        self.generation = generation
        self.resource_capacities = [
            Resource(ResourceType.FOOD, 10),
            Resource(ResourceType.WATER, 10),
            Resource(ResourceType.IRON, 10),
            Resource(ResourceType.DIAMONDS, 0),
            Resource(ResourceType.GOLD, 0),
            Resource(ResourceType.CARBON, 0),
            Resource(ResourceType.FUEL, 0),
            Resource(ResourceType.ENERGY, 100),
        ]

    def resource_capacity(self, resource_type: ResourceType) -> int:
        Character_resource_capacity = self.get_resource_capacity(resource_type)
        building_resource_capacity = self.current_region.get_resource_capacity(self, resource_type)
        return building_resource_capacity + Character_resource_capacity
    
    def get_resource_capacity(self, resource_type: ResourceType) -> Resource:
        for res in self.resource_capacities:
            if res.type == resource_type:
                return res
