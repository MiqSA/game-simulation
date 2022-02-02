from app.main.services.manager_files import JsonFiles
from app.main.config import *
import random




class LandModel:
    @classmethod
    def parameters(cls):
        parameters = {
            'board_position': [],
            'sale_value': [],
            'rent_value': [],
            'owner': None
        }
        return parameters

    @classmethod
    def initialize(cls):
        files = JsonFiles(PATH_FILES, FILENAME_LANDS)
        if files.read() is False:
            files.new()

        files.clear()

    @classmethod
    def first_conditions(cls):
        files = JsonFiles(PATH_FILES, FILENAME_LANDS)
        data = []

        for position in range(TOTAL_BOARD_POSITIONS):
            parameters = LandModel.parameters()

            parameters['board_position'] = position
            value = int(position * 10000 + 100000 * random.random())
            parameters['sale_value'] = value
            parameters['rent_value'] = int(0.01 * value)

            data.append(parameters)


        files.new(data=data)


