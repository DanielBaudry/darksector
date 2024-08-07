from domain.building import BuildingTemplate
from domain.resources import Resource


class CityBuilding(BuildingTemplate):
    city: "City"

    def __init__(self, name: str, construction_time: int, construction_costs: list[Resource], resource_capacities: list[Resource], generation: list[Resource], city: "City") -> None:
        super().__init__(name, construction_time, construction_costs, resource_capacities, generation)
        self.city = city

    @staticmethod
    def from_building(building: BuildingTemplate, city: "City") -> "CityBuilding":
        return CityBuilding(
            building.name,
            building.construction_time,
            building.construction_costs,
            building.resource_capacities,
            building.generation,
            city
        )
