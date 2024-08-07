from typing import Optional
from domain.resources import Resource, ResourceType


class BaseCharacter:
    name: str
    resources: list[Resource]
    current_region: "Region"
    cities: list["City"]

    def __init__(self, name: str, resources: list[Resource], current_region: Optional["Region"] = None, cities: Optional[list["City"]] = None) -> None:
        self.name = name
        self.resources = resources
        # TODO: resource_capacities to rework
        self.resource_capacities = [
            Resource(ResourceType.FOOD, 100),
            Resource(ResourceType.WATER, 100),
            Resource(ResourceType.IRON, 100),
            Resource(ResourceType.DIAMONDS, 100),
            Resource(ResourceType.GOLD, 100),
            Resource(ResourceType.CARBON, 100),
            Resource(ResourceType.FUEL, 100),
            Resource(ResourceType.ENERGY, 0),
        ]
        self.current_region = current_region
        self.cities = [] if cities is None else cities

    def add_city(self, city: "City") -> None:
        self.cities.append(city)

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
