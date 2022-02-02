from app.main.services.config_print import bcolors
from app.main.controllers.players_controller import Players
from app.main.controllers.lands_controller import Lands



class BankGame:

    @classmethod
    def initialize(cls):
        Lands.initialize()
        Players.initialize()


    @classmethod
    def new_match(cls):
        Players.first_conditions()
        Lands.first_conditions()
        print(f"{bcolors.OKCYAN}      New match {bcolors.ENDC}")

    @classmethod
    def sort_players(cls):
        sorted_players = Players.sorted_players()
        return sorted_players

    @classmethod
    def save_match(cls):
        print('Salva dados da partida')

    @classmethod
    def play(cls, timeout):
        game_round = 1
        while game_round <= timeout:

            print(f'>>> {game_round} Round ')

            for player in range(4):
                print(f'     \n>>> Player {player} joga o dado ')
                print(f'     >>> Avança o número de casas resultante do dado ')
                print(f'     >>> Verifica se está disponível a propriedade atual ')
                print(f'     >>> Se estiver disponível ')
                print(f'          >>>>> De acordo com o perfil decide se compra ou não a propriedade')
                print(f'     >>> Senão')
                print(f'          >>>>> Pagar ao proprietário')
                print(f'     >>> Atualiza parametros do jogador e propriedade')
                print(f'     >>> Elimina perdedores')
                print(f'     >>> Se Existe vencedor')
                print(f'          >>>>> Termina partida')
                print(f'     >>> Senão')
                print(f'          >>>>> Continua partida')
            print(f'     >>> Soma número de rodadas efetuadas na partida')
            game_round += 1
            print(f'     >>> Se o número de rodadas efetuadas é maior que o timeout então termina a partida')
            print(f'     >>> Senão continua ')
            cls.save_match()
            print(f"{bcolors.OKGREEN} ----- {bcolors.ENDC}" * 5)