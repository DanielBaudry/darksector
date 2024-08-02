from domain.buildings import Building
from domain.region import Region
from domain.resources import Resource, ResourceType


class CharacterRegion:
    region: Region
    buildings: list[Building]

    def __init__(self, region: Region, buildings: list[Building]) -> None:
        self.region = region
        self.buildings = buildings

    def get_resource_capacity(self, resource_type: ResourceType) -> Resource:
        total_resource_capacity = Resource(resource_type, 0)
        for building in self.buildings:
            total_resource_capacity += building.get_resource_capacity(resource_type)
        return total_resource_capacity
