import time
import threading

from domain.action import ScavengeAction
from domain.building import BuildingTemplate
from domain.character import PlayerCharacter
from domain.city import City
from domain.drop_table import DropRate, DropTable
from domain.region import Region
from domain.resources import Resource, ResourceType
from use_cases.create_new_building_in_region import CreateNewBuildingInRegion

# Create a lock
lock = threading.Lock()

def generate_resources(character):
    for city in character.cities:
        for building in city.buildings:
            for resource in building.generation:
                character.add_resource_amount(resource)
    for resource in character.generation:
        character.add_resource_amount(resource)


def consume_resources(character):
    for consumption in character.consumptions:
        character.remove_resource_amount(consumption)


def compute_resources(character):
    while True:
        with lock:
            generate_resources(character)
            consume_resources(character)

            # Wait for a minute
            time.sleep(5)


def main():
    region_1 = Region(
        name="Region 1",
        resources_probabilities=[
            DropTable(
                resource_type=ResourceType.FOOD,
                drop_rates=[
                    DropRate(probability=50, min_amount=1, max_amount=2),
                    DropRate(probability=50, min_amount=3, max_amount=5)
                ]
            ),
            DropTable(
                resource_type=ResourceType.WATER,
                drop_rates=[
                    DropRate(probability=50, min_amount=1, max_amount=2),
                    DropRate(probability=50, min_amount=3, max_amount=5)
                ]
            ),
            DropTable(
                resource_type=ResourceType.GOLD,
                drop_rates=[
                    DropRate(probability=2, min_amount=1, max_amount=2),
                    DropRate(probability=4, min_amount=3, max_amount=5)
                ]
            )
        ]
    )

    character = PlayerCharacter(
        name="Dan",
        consumptions=[Resource(ResourceType.FOOD, 1),
                      Resource(ResourceType.WATER, 1)],
        generation=[Resource(ResourceType.ENERGY, 40)],
        resources=[
            Resource(ResourceType.FOOD, 10),
            Resource(ResourceType.WATER, 10),
            Resource(ResourceType.IRON, 10),
            Resource(ResourceType.DIAMONDS, 0),
            Resource(ResourceType.GOLD, 0),
            Resource(ResourceType.CARBON, 0),
            Resource(ResourceType.FUEL, 0),
            Resource(ResourceType.ENERGY, 100)
        ],
        current_region=region_1,
    )

    hutte = BuildingTemplate(
        name="hutte",
        construction_time=10,
        construction_costs=[],
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
        generation=[],
    )

    CreateNewBuildingInRegion().execute(
        region=region_1,
        character=character,
        building=hutte,
    )

    scavenge_action = ScavengeAction()
    
    compute_resources_thread = threading.Thread(target=compute_resources, args=(character,))
    compute_resources_thread.start()

    while True:
        # Player input
        action = input("Enter an action (e.g., 'build', 'scavenge', 'show'): ")

        if action == "build":
            # Handle building actions
            print("Building actions")
        elif action == "scavenge" or action == "s":
            scavenge_action.execute(character, region_1)
        elif action == "show":
            print("Player:", character.name)
            for city in character.cities:
                print(city.name)
                for building in city.buildings:
                    print(building.name)
        else:
            print("Invalid action")
    
        print("---")
        for res in character.resources:
            print(res.type.name, res.amount)
        print("---")



if __name__ == "__main__":
    main()
