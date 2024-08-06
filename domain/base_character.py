from domain.character_region import CharacterRegion
from domain.resources import Resource, ResourceType


class BaseCharacter:
    name: str
    resources: list[Resource]
    current_region: CharacterRegion

    def __init__(self, name: str, resources: list[Resource], current_region: CharacterRegion) -> None:
        self.name = name
        self.resources = resources
        self.current_region = current_region

    def get_resource(self, resource_type: ResourceType) -> Resource:
        for res in self.resources:
            if res.type == resource_type:
                return res

    def add_resource_amount(self, resource: Resource) -> None:
        Character_resource = self.get_resource(resource.type)
        resource_capacity = self.resource_capacity(resource_type=resource.type)
        Character_resource.amount = min(resource_capacity.amount, Character_resource.amount + resource.amount)

    def remove_resource_amount(self, resource: Resource) -> None:
        Character_resource = self.get_resource(resource.type)
        Character_resource.amount = max(0, Character_resource.amount - resource.amount)
