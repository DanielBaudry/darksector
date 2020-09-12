from domain.gear.gear import Gear


class PlayerGear:
    def __init__(self,
                 gear: Gear,
                 is_equipped: bool = False):
        self.gear = gear
        self.is_equipped = is_equipped
