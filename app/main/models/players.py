from app.main.services.manager_files import JsonFiles
from app.main.config import *
import random



class PlayerModel:
    @classmethod
    def parameters(cls):
        parameters = {
            'id': None,
            'position': None,
            'balance_value': 0,
            'profile': None,
            'activate': 1 # 0 is False and 1 and True
        }
        return parameters

    @classmethod
    def initialize(cls):
        files = JsonFiles(PATH_FILES, FILENAME_PLAYERS)

        if files.read() is False:
            files.new()

        files.clear()

    @classmethod
    def first_conditions(cls):
        files = JsonFiles(PATH_FILES, FILENAME_PLAYERS)
        data = []
        for position in range(1, TOTAL_PLAYERS+1):
            parameters = PlayerModel.parameters()

            parameters['id'] = position
            parameters['profile'] = position
            parameters['balance_value'] = 300

            data.append(parameters)
        files.new(data=data)


    @classmethod
    def read_player(cls, id):
        files = JsonFiles(PATH_FILES, FILENAME_PLAYERS)
        all_players = files.read()
        player = all_players[id-1]
        return player


    @classmethod
    def read_players(cls):
        files = JsonFiles(PATH_FILES, FILENAME_PLAYERS)
        all_players = files.read()
        return all_players



    @classmethod
    def update_player(cls, id, update_data):
        files = JsonFiles(PATH_FILES, FILENAME_PLAYERS)
        all_players = files.read()
        all_players[id-1] = update_data
        files.new(data=all_players)
