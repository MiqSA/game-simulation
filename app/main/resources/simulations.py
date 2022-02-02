from app.main.services.config_print import printProgressBar, bcolors
from app.main.controllers.games_controller import BankGame
from app.main.services.manager_files import JsonFiles
from app.main.config import PATH_FILES, FILENAME_RESULTS





class Simulation():
    def __init__(self, parameters):
        self.game = parameters.get('game')
        self.iterations = parameters.get('iterations', 300)
        self.timeout = parameters.get('timeout', 1000)

    @classmethod
    def initialize(cls):
        files = JsonFiles(PATH_FILES, FILENAME_RESULTS)
        if files.read() is False:
            files.new()
        files.clear()


    def create(self):
        try:
            self.initialize()
            BankGame.initialize()

            print(f"{bcolors.HEADER} Created enviroment simulation game with success! {bcolors.ENDC} \n")

        except Exception as err:
            print(f"{bcolors.WARNING} Error Dont created simulation game! {bcolors.ENDC}")

    def loop(self):
        try:
            for iteration in range(self.iterations):
                print(f"{bcolors.OKCYAN}> {iteration+1}. Simulation{bcolors.ENDC}")


                BankGame.new_match()
                BankGame.sort_players()
                # BankGame.play(self.timeout)

        except Exception as err:
            print('Loop doesnt work!',err)

    def results(self):
        try:
            print(f"{bcolors.OKGREEN}>>>> Simulation results <<<<{bcolors.ENDC}")
        except Exception as err:
            print('Error in imulation results!', err)


    def run(self):
        self.create()
        self.loop()
        self.results()