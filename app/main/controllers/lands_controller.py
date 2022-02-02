from app.main.services.config_print import bcolors
from app.main.models.lands import LandModel



class Lands:
    @classmethod
    def initialize(cls):
        LandModel.initialize()

    @classmethod
    def first_conditions(cls):
        LandModel.first_conditions()
        print(f"{bcolors.OKCYAN}      Update parameters to all lands - First conditions {bcolors.ENDC}")
