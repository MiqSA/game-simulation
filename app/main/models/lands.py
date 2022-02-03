from app.main.services.manager_files import JsonFiles
from app.main.config import PATH_FILES, FILENAME_LANDS, TOTAL_BOARD_POSITIONS
import random

files = JsonFiles(PATH_FILES, FILENAME_LANDS)


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
        if files.read() is False:
            files.new()

        files.clear()

    @classmethod
    def first_conditions(cls):
        data = []

        for position in range(1, TOTAL_BOARD_POSITIONS+1):
            parameters = LandModel.parameters()

            parameters['board_position'] = position
            value = int(random.randint(1, 300) + random.randint(1,200) * random.random())
            parameters['sale_value'] = value
            parameters['rent_value'] = int(0.1 * value)
            data.append(parameters)

        files.new(data=data)

    @classmethod
    def read_lands(cls, id):
        all_lands = files.read()
        land = all_lands[id - 1]
        return land


    @classmethod
    def update_land(cls, id, update_data):
        all_lands = files.read()
        all_lands[id-1] = update_data
        files.new(data=all_lands)


