import time
import threading

from domain.action import ScavengeAction
from domain.buildings import Building
from domain.character import Character
from domain.drop_table import DropRate, DropTable
from domain.region import Region
from domain.resources import Resource, ResourceType

# Create a lock
lock = threading.Lock()

def generate_resources(character):
    while True:
        # Generate resources
        with lock:
            for building in character.buildings:
                for resource in building.generation:
                    character.add_resource_amount(resource)
            for resource in character.generation:
                character.add_resource_amount(resource)

        # Wait for a minute
        time.sleep(5)

def consume_resources(character):
    while True:
        # Consume resources
        with lock:
            for consumption in character.consumptions:
                character.remove_resource_amount(consumption)

        # Wait for a minute
        time.sleep(5)

def main():
    hutte = Building(
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

    character = Character(
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
        buildings=[
            hutte
        ]
    )

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

    scavenge_action = ScavengeAction()
    
    # Create threads for resource generation and consumption
    generate_thread = threading.Thread(target=generate_resources, args=(character,))
    consume_thread = threading.Thread(target=consume_resources, args=(character,))

    # Start the threads
    generate_thread.start()
    consume_thread.start()

    while True:
        # Player input
        action = input("Enter an action (e.g., 'build', 'gather', 'trade'): ")

        if action == "build":
            # Handle building actions
            print("Building actions")
        elif action == "scavenge" or action == "s":
            scavenge_action.execute(character, region_1)
        elif action == "trade":
            # Handle trading actions
            print("Trading actions")
        else:
            print("Invalid action")

        print("---")
        for res in character.resources:
            print(res.type.name, res.amount)
        print("---")

if __name__ == "__main__":
    main()
