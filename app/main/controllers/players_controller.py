from app.main.services.config_print import bcolors
from app.main.models.players import PlayerModel
from app.main.models.profiles import PlayersProfiles
from app.main.config import TOTAL_PLAYERS, TOTAL_BOARD_POSITIONS
import random



class Players:
    @classmethod
    def initialize(cls):
        PlayerModel.initialize()

    @classmethod
    def sorted_players(cls):
        sort_players = random.sample(range(1, TOTAL_PLAYERS+1), TOTAL_PLAYERS)
        return sort_players

    @classmethod
    def get_player(cls,id):
        player = PlayerModel.read_player(id)
        return player

    @classmethod
    def get_players(cls):
        players = PlayerModel.read_players()
        return players


    @classmethod
    def update_player(cls, id, update_data):
        PlayerModel.update_player(id, update_data)


    @classmethod
    def first_conditions(cls):
        PlayerModel.first_conditions()

    @classmethod
    def play_dice(cls):
        return random.randint(1,6)


    @classmethod
    def move_to(cls, player):
        info_player = Players.get_player(player)
        advance = Players.play_dice()
        position = info_player['position']


        # Update informations
        if position is None:
            position = 0

        position = position + advance
        if position > TOTAL_BOARD_POSITIONS:
            position = position - TOTAL_BOARD_POSITIONS
            info_player['balance_value'] = info_player['balance_value'] + 100

        info_player['position'] = position
        Players.update_player(player, info_player)
        return position

    @classmethod
    def buy_or_not(cls, board_position, id_player):
        decision = PlayersProfiles(board_position, id_player).buy_according_profile()
        return decision




