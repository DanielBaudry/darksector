from typing import Optional
from domain.building import BuildingTemplate
from domain.character import PlayerCharacter
from domain.city import City
from domain.city_building import CityBuilding
from domain.region import Region


class CreateNewCityInRegion:
    def execute(
        self, character: PlayerCharacter, building: BuildingTemplate, region: Region
    ) -> None:
        if character.current_region != region:
            # TODO: raise exception or handle this case
            return

        city_in_region = self.find_character_city_in_region(character, region)

        if city_in_region:
            # TODO: raise exception or handle this case
            return

        city_in_region = City(character, region)

        print(f"{character.name} constructed a new City in {region.name}.")

    def find_character_city_in_region(
        self, character: PlayerCharacter, region: Region
    ) -> Optional["City"]:
        for city in region.cities:
            if city.character == character:
                return city
        return None
