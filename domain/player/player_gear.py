from typing import Optional

from domain.gear.gear import Gear


class PlayerGear:
    def __init__(self,
                 gear: Gear,
                 identifier: Optional[int] = None,
                 is_equipped: bool = False):
        self.identifier = identifier
        self.gear = gear
        self.is_equipped = is_equipped
