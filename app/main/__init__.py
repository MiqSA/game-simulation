from app.main.resources.simulations import Simulation
from app.main.controllers.games import BankGame



def game_bank_simulation():
    parameters = {
        'game': BankGame(),
        'iterations': 2,
        'timeout': 2
    }
    Simulation(parameters).run()





