from domain.resources import Resource, ResourceType


class Building:
    name: str
    construction_time: int
    construction_costs: list[Resource]
    generation: list[Resource]
    resource_capacities: list[Resource]

    def __init__(self, name: str, construction_time: int, construction_costs: list[Resource], resource_capacities: list[Resource], generation: list[Resource]):
        self.name = name
        self.construction_time = construction_time
        self.construction_costs = construction_costs
        self.resource_capacities = resource_capacities
        self.generation = generation

    def get_resource_capacity(self, resource_type: ResourceType) -> Resource:
        for res in self.resource_capacities:
            if res.type == resource_type:
                return res
