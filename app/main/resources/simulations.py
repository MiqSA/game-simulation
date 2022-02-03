from app.main.services.config_print import bcolors,printProgressBar
from app.main.controllers.games_controller import BankGame
from app.main.controllers.simulation_controller import OutputSimulation
from app.main.config import ITERATIONS, TIMEOUT
import time



class Simulation:
    def __init__(self):
        self.iterations = ITERATIONS
        self.timeout = TIMEOUT


    def create(self):
        try:
            OutputSimulation.initialize()
            BankGame.initialize()
        except Exception as err:
            print(f"{bcolors.WARNING} Error Dont created simulation game! {bcolors.ENDC}")

    def loop(self):
        try:
            printProgressBar(0, self.iterations, prefix='Progress:', suffix='Complete', length=50)
            for iteration in range(self.iterations):

                BankGame.new_match()
                sorted_players = BankGame.sort_players()
                BankGame.play(self.timeout, sorted_players)

                time.sleep(0.1)

                # Update Progress Bar
                printProgressBar(iteration + 1, self.iterations, prefix='Progress:', suffix='Complete', length=50)

        except Exception as err:
            print(f"{bcolors.WARNING} Loop doesnt work!! {bcolors.ENDC}", err)

    def results(self):
        try:
            print(f"{bcolors.OKGREEN}>>>> Resultados da Simulação <<<<{bcolors.ENDC}")
            OutputSimulation.show_results()
        except Exception as err:
            print('Error in simulation results!', err)

    def run(self):
        self.create()
        self.loop()
        self.results()