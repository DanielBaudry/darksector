from domain.building import BuildingTemplate
from domain.character import PlayerCharacter
from domain.city import City
from domain.city_building import CityBuilding
from domain.region import Region


class CreateNewBuildingInRegion:
    def execute(self, character: PlayerCharacter, building: BuildingTemplate, region: Region) -> None:
        if character.current_region != region:
            # TODO: raise exception or handle this case
            return
    
        for cost in building.construction_costs:
            if character.get_resource_capacity(cost.type).amount < cost.amount:
                # TODO: raise exception or handle this case
                return

        for cost in building.construction_costs:
            character.remove_resource_amount(cost)

        city_in_region = None

        for city in region.cities:
            if city.character == character:
                city_in_region = city
                break
        
        if not city_in_region:
            city_in_region = City("New City", character, region)
            character.add_city(city_in_region)
            region.add_city(city_in_region)

        new_building = CityBuilding.from_building(building, city_in_region)
        city_in_region.add_building(new_building)

        print(f"{character.name} constructed {building.name} in {region.name}.")
