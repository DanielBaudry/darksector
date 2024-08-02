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

    def __add__(self, other: "Resource") -> "Resource":
        if self.type == other.type:
            return Resource(self.type, self.amount + other.amount)
        else:
            raise ValueError(f"Cannot add resources of different types: {self.type} and {other.type}")

    def __sub__(self, other: "Resource") -> "Resource":
        if self.type == other.type:
            return Resource(self.type, max(0, self.amount - other.amount))
        else:
            raise ValueError(f"Cannot subtract resources of different types: {self.type} and {other.type}")
