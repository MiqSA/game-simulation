from app.main.services.config_print import bcolors

from app.main.models.players import PlayerModel
from app.main.config import TOTAL_PLAYERS
import random



class Players:
    @classmethod
    def initialize(cls):
        PlayerModel.initialize()

    @classmethod
    def sorted_players(cls):
        sort_players = random.sample(range(TOTAL_PLAYERS), TOTAL_PLAYERS)
        print(f"{bcolors.OKCYAN}      Players sorted {bcolors.ENDC}- {sort_players}")
        return sort_players



    @classmethod
    def first_conditions(cls):
        PlayerModel.first_conditions()
        print(f"{bcolors.OKCYAN}      Update parameters to all players - First conditions {bcolors.ENDC}")




