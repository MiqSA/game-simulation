from app.main.services.manager_files import JsonFiles
from app.main.config import PATH_FILES, FILENAME_RESULTS, ITERATIONS

files = JsonFiles(PATH_FILES, FILENAME_RESULTS)

class OutputSimulationModel:
    @classmethod
    def parameters(cls):
        parameters = {
            'total_timeout_matches': 0,
            'total_rounds_by_matche': 0,
            'average_rounds_by_matche':0,
            'count_winners': {
                1: 0,
                2: 0,
                3: 0,
                4: 0}}
        parameters['greater_winner'] = max(parameters['count_winners'], key=parameters['count_winners'].get)
        return parameters

    @classmethod
    def first_conditions(cls):
        parameters = cls.parameters()
        files.new(data=parameters)


    @classmethod
    def initialize(cls):
        if files.read() is False:
            files.new()
        files.clear()

    @classmethod
    def read_results(cls):
        return files.read()

    @classmethod
    def update_results(cls, game_round, id_winner, timeout):
        results = cls.read_results()
        if game_round > timeout:
            results['total_timeout_matches'] = results['total_timeout_matches'] + 1

        results['total_rounds_by_matche'] = results['total_rounds_by_matche'] + game_round
        results['average_rounds_by_matche'] = int(results['total_rounds_by_matche'] / ITERATIONS)
        results['count_winners'][str(id_winner)] =  results['count_winners'][str(id_winner)] + 1
        results['greater_winner'] = max(results['count_winners'], key=results['count_winners'].get)
        return files.new(results)
