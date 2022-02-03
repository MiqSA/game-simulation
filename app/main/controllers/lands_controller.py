from app.main.services.config_print import bcolors
from app.main.models.lands import LandModel



class Lands:
    @classmethod
    def initialize(cls):
        LandModel.initialize()

    @classmethod
    def first_conditions(cls):
        LandModel.first_conditions()

    @classmethod
    def check_land_is_available(cls, id):
        land = LandModel.read_lands(id)
        if land['owner'] is None:
            return True
        else:
            return False

    @classmethod
    def get_land(cls,id):
        land = LandModel.read_lands(id)
        return land

    @classmethod
    def update_land(cls, id, update_data):
        LandModel.update_land(id, update_data)


