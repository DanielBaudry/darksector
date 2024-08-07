from typing import Optional
from domain.drop_table import DropTable
from domain.resources import Resource, ResourceType


class Region:
    name: str
    resources_probabilities: list[DropTable]
    characters: list["BaseCharacter"]
    cities: list["City"]

    def __init__(self, name: str, resources_probabilities: list[DropTable], characters: Optional[list["BaseCharacter"]] = None, cities: Optional[list["City"]] = None) -> None:
        self.name = name
        self.resources_probabilities = resources_probabilities
        self.characters = [] if characters is None else characters
        self.cities = [] if cities is None else cities

    def add_city(self, city: "City") -> None:
        self.cities.append(city)

    def generate_resources(self) -> list[Resource]:
        resources = []
        for drop_table in self.resources_probabilities:
            resources.append(drop_table.generate_drop())
        return resources

    def get_resource_capacity(self, character: "BaseCharacter", resource_type: ResourceType) -> Resource:
        total_resource_capacity = Resource(resource_type, 0)
        for city in self.cities:
            if city.character == character:
                for building in city.buildings:
                    total_resource_capacity += building.get_resource_capacity(resource_type)
        return total_resource_capacity
