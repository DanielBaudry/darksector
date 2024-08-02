from abc import ABC, abstractmethod


class Action(ABC):
    name: str

    @abstractmethod
    def execute(self, character, *args, **kwargs):
        pass

class ScavengeAction(Action):
    def __init__(self) -> None:
        self.name = "Scavenge"

    def execute(self, character, *args, **kwargs):
        # get region from args
        region = args[0]

        # generate resources
        generated_resources = region.generate_resources()
        print(generated_resources)

        # add resources to character's inventory
        for res in generated_resources:
            print(res.type.name, res.amount, "added to inventory")
            character.add_resource_amount(res)

        print(f"Scavenged resources from {region}")
