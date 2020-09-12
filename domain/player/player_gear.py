from domain.gear.gear import Gear


class PlayerGear:
    def __init__(self,
                 gear: Gear,
                 amount: int):
        self.gear = gear
        self.amount = amount
