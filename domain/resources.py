from enum import Enum


class ResourceType(Enum):
    WATER = "water"
    FOOD = "food"
    IRON = "iron"
    DIAMONDS = "diamonds"
    GOLD = "gold"
    CARBON = "carbon"
    FUEL = "fuel"
    ENERGY = "energy"

class Resource:
    def __init__(self, type: ResourceType, amount: int):
        self.type = type
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.type.name}: {self.amount}"
