from domain.drop_table import DropTable
from domain.resources import Resource


class Region:
    name: str
    resources_probabilities: list[DropTable]

    def __init__(self, name, resources_probabilities) -> None:
        self.name = name
        self.resources_probabilities = resources_probabilities

    def generate_resources(self) -> list[Resource]:
        resources = []
        for drop_table in self.resources_probabilities:
            resources.append(drop_table.generate_drop())
        return resources
