from typing import Optional
from domain.city_building import CityBuilding
from domain.region import Region
from domain.resources import Resource, ResourceType


class City:
    name: str
    character: "BaseCharacter"
    region: Region
    buildings: list[CityBuilding]

    def __init__(self, name: str, character: "BaseCharacter", region: Region, buildings: Optional[list[CityBuilding]] = None) -> None:
        self.name = name
        self.character = character
        self.region = region
        self.buildings = [] if not buildings else buildings

    def get_resource_capacity(self, resource_type: ResourceType) -> Resource:
        total_resource_capacity = Resource(resource_type, 0)
        for building in self.buildings:
            total_resource_capacity += building.get_resource_capacity(resource_type)
        return total_resource_capacity

    def add_building(self, building: CityBuilding) -> None:
        self.buildings.append(building)
