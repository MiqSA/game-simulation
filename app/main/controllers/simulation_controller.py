from app.main.services.config_print import bcolors
from app.main.models.output_simulations import OutputSimulationModel
from app.main.config import ITERATIONS



class OutputSimulation:
    @classmethod
    def initialize(cls):
        OutputSimulationModel.initialize()
        OutputSimulationModel.first_conditions()

    @classmethod
    def update_results(cls,game_round, id_winner, timeout):
        OutputSimulationModel.update_results(game_round, id_winner, timeout)


    @classmethod
    def read_results(cls):
        results = OutputSimulationModel.read_results()
        return results

    @classmethod
    def show_results(cls):
        results = OutputSimulationModel.read_results()
        profiles = {
            1: 'Jogador impulsivo',
            2: 'Jogador exigente',
            3: 'Jogador cauteloso',
            4: 'Jogador aleatório'
        }

        print(f"{bcolors.OKBLUE} - Partidas terminadas por timeout (1000 rodadas): {bcolors.ENDC}",
              results['total_timeout_matches'])
        print(f"{bcolors.OKBLUE} - Quantidade de turnos em média demora uma partida: {bcolors.ENDC}",
              results['average_rounds_by_matche'])
        print(f"{bcolors.OKBLUE} - Porcentagem de vitórias por comportamento dos jogadores: {bcolors.ENDC}")

        for profile in profiles:
            value = 100*results['count_winners'][f'{profile}']/ITERATIONS
            print(f"{bcolors.OKCYAN}    - {value}% {profiles[profile]}{bcolors.ENDC}")

        print(f"{bcolors.OKBLUE} - Comportamento que mais vence: {bcolors.ENDC}",
              profiles[int(results['greater_winner'])])
        return results

