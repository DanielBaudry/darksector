from domain.building import BuildingTemplate
from domain.character import PlayerCharacter
from domain.region import Region
from domain.resources import Resource, ResourceType
from tests.generator import create_test_building_template, create_test_character
from use_cases.create_new_building_in_region import CreateNewBuildingInRegion


def test_should_not_allow_construction_in_different_region():
    # Arrange
    character = create_test_character()
    building = create_test_building_template()
    initial_region = Region("InitialRegion", resources_probabilities=[])
    character.current_region = initial_region
    different_region = Region("DifferentRegion", resources_probabilities=[])

    create_new_building_in_region_use_case = CreateNewBuildingInRegion()

    # Act
    create_new_building_in_region_use_case.execute(character, building, different_region)

    # Assert
    assert character.current_region == initial_region
    assert len(character.cities) == 0
    assert len(different_region.cities) == 0

def test_should_not_allow_construction_if_resource_capacity_is_insufficient():
    # Arrange
    character = create_test_character()
    building = create_test_building_template()
    region = Region("TestRegion", resources_probabilities=[])
    character.current_region = region

    # Set insufficient resource capacity
    resource_type = building.construction_costs[0].type
    character.add_resource_amount(Resource(resource_type, -character.get_resource(resource_type).amount))

    create_new_building_in_region_use_case = CreateNewBuildingInRegion()

    # Act
    create_new_building_in_region_use_case.execute(character, building, region)

    # Assert
    assert character.current_region == region
    assert len(character.cities) == 0
    assert len(region.cities) == 0

def test_should_add_new_building_to_city_in_specified_region():
    # Arrange
    character = create_test_character(resources=[
        Resource(ResourceType.FOOD, 0),
        Resource(ResourceType.WATER, 0),
        Resource(ResourceType.IRON, 10),
        Resource(ResourceType.DIAMONDS, 0),
        Resource(ResourceType.GOLD, 0),
        Resource(ResourceType.CARBON, 0),
        Resource(ResourceType.FUEL, 0),
        Resource(ResourceType.ENERGY, 0)
    ])
    building = create_test_building_template(
        construction_costs=[
            Resource(ResourceType.IRON, 5),
        ]
    )
    region = Region("TestRegion", resources_probabilities=[])
    character.current_region = region

    create_new_building_in_region_use_case = CreateNewBuildingInRegion()

    # Act
    create_new_building_in_region_use_case.execute(character, building, region)

    # Assert
    assert len(character.cities) == 1
    assert len(region.cities) == 1
    assert len(character.cities[0].buildings) == 1


def test_should_remove_construction_costs_from_character_resources():
    # Arrange
    character = create_test_character(resources=[
        Resource(ResourceType.FOOD, 0),
        Resource(ResourceType.WATER, 0),
        Resource(ResourceType.IRON, 10),
        Resource(ResourceType.DIAMONDS, 0),
        Resource(ResourceType.GOLD, 0),
        Resource(ResourceType.CARBON, 0),
        Resource(ResourceType.FUEL, 0),
        Resource(ResourceType.ENERGY, 0)
    ])
    building = create_test_building_template(
        construction_costs=[
            Resource(ResourceType.IRON, 5),
        ]
    )
    region = Region("TestRegion", resources_probabilities=[])
    character.current_region = region

    create_new_building_in_region_use_case = CreateNewBuildingInRegion()

    # Act
    create_new_building_in_region_use_case.execute(character, building, region)

    # Assert
    assert character.get_resource(ResourceType.IRON).amount == 5
