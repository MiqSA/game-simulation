from app.main.services.manager_files import JsonFiles
from app.main.config import *
import random



class PlayerModel:
    @classmethod
    def parameters(cls):
        parameters = {
            'id': None,
            'complete_way': None,
            'balance_value': None,
            'profile': None
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

        for position in range(TOTAL_PLAYERS):
            parameters = PlayerModel.parameters()

            parameters['id'] = position
            parameters['profile'] = position

            data.append(parameters)


        files.new(data=data)




class PlayersProfiles:
    def type_1(self):
        pass

    def type_2(self):
        pass

    def type_3(self):
        pass

    def type_4(self):
        pass

    def get(self, profile_id):
        profiles = {
            0: self.type_1(),
            1: self.type_2(),
            2: self.type_3(),
            3: self.type_4()
        }

        return profiles[profile_id]







class PlayersInformation:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename


    def new(self):
        pass

    def list(self):
        pass

    def update(self, id):
        pass

    def delete(self, id):
        pass




