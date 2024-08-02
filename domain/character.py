from domain.charcater_region import CharacterRegion
from domain.resources import Resource, ResourceType


class Character:
    name: str
    consumptions: list[Resource]
    generation: list[Resource]
    resources: list[Resource]
    current_region: CharacterRegion

    def __init__(self, name: str, consumptions: list[Resource], generation: list[Resource], resources: list[Resource], current_region: CharacterRegion) -> None:
        self.name = name
        self.consumptions = consumptions
        self.generation = generation
        self.resources = resources
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
        self.current_region = current_region

    def resource_capacity(self, resource_type: ResourceType) -> int:
        Character_resource_capacity = self.get_resource_capacity(resource_type)
        building_resource_capacity = self.current_region.get_resource_capacity(resource_type)
        return building_resource_capacity + Character_resource_capacity
    
    def get_resource(self, resource_type: ResourceType) -> Resource:
        for res in self.resources:
            if res.type == resource_type:
                return res
    
    def get_resource_capacity(self, resource_type: ResourceType) -> Resource:
        for res in self.resource_capacities:
            if res.type == resource_type:
                return res

    def add_resource_amount(self, resource: Resource) -> None:
        Character_resource = self.get_resource(resource.type)
        resource_capacity = self.resource_capacity(resource_type=resource.type)
        Character_resource.amount = min(resource_capacity.amount, Character_resource.amount + resource.amount)

    def remove_resource_amount(self, resource: Resource) -> None:
        Character_resource = self.get_resource(resource.type)
        Character_resource.amount = max(0, Character_resource.amount - resource.amount)
