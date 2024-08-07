import random
from domain.resources import Resource, ResourceType


class DropRate:
    probability: float
    min_amount: int
    max_amount: int

    def __init__(
        self,
        probability: int,
        min_amount: int,
        max_amount: int,
    ) -> None:
        self.probability = probability
        self.min_amount = min_amount
        self.max_amount = max_amount


class DropTable:
    resource_type: ResourceType
    drop_rates: list[DropRate]

    def __init__(self, resource_type: ResourceType, drop_rates: list[DropRate]) -> None:
        total_probability = sum(drop_rate.probability for drop_rate in drop_rates)
        if total_probability > 100:
            raise ValueError("Total probability must not exceed 100%")
        self.resource_type = resource_type
        self.drop_rates = drop_rates

    def generate_drop(self) -> Resource:
        random_number = random.uniform(0, 100)
        total_probability = 0

        for drop_rate in self.drop_rates:
            total_probability += drop_rate.probability
            if random_number <= total_probability:
                return Resource(self.resource_type, random.randint(drop_rate.min_amount, drop_rate.max_amount))
        return Resource(self.resource_type, 0)
