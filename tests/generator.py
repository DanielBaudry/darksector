from domain.building import BuildingTemplate
from domain.character import PlayerCharacter
from domain.resources import Resource, ResourceType

def create_test_character(resources: list = [
        Resource(ResourceType.FOOD, 10),
        Resource(ResourceType.WATER, 10),
        Resource(ResourceType.IRON, 10),
        Resource(ResourceType.DIAMONDS, 0),
        Resource(ResourceType.GOLD, 0),
        Resource(ResourceType.CARBON, 0),
        Resource(ResourceType.FUEL, 0),
        Resource(ResourceType.ENERGY, 100)
    ]) -> PlayerCharacter:
    """
    This function creates a test character for testing purposes.

    Parameters:
    None

    Returns:
    PlayerCharacter: A PlayerCharacter instance with default attributes for testing.
    """
    return PlayerCharacter(
        "TestCharacter",
        consumptions=[Resource(ResourceType.FOOD, 1),
                      Resource(ResourceType.WATER, 1)],
        generation=[Resource(ResourceType.ENERGY, 40)],
        resources=resources,
    )

def create_test_building_template(construction_costs: list = [
        Resource(ResourceType.IRON, 10),
    ]) -> BuildingTemplate:
    """
    This function creates a test building template for testing purposes.

    Parameters:
    None

    Returns:
    BuildingTemplate: A BuildingTemplate instance with default attributes for testing.
    """
    return BuildingTemplate(
        "Well",
        construction_time=20,
        construction_costs=construction_costs,
        resource_capacities=[
            Resource(ResourceType.FOOD, 50),
            Resource(ResourceType.WATER, 50),
            Resource(ResourceType.IRON, 50),
            Resource(ResourceType.DIAMONDS, 10),
            Resource(ResourceType.GOLD, 10),
            Resource(ResourceType.CARBON, 0),
            Resource(ResourceType.FUEL, 0),
            Resource(ResourceType.ENERGY, 0)
        ],
        generation=[
            Resource(ResourceType.WATER, 20),
        ],
    )
