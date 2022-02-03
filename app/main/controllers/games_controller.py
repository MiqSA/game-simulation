from app.main.services.config_print import bcolors
from app.main.controllers.players_controller import Players
from app.main.controllers.lands_controller import Lands
from app.main.controllers.simulation_controller import OutputSimulation

from app.main.config import TOTAL_PLAYERS



class BankGame:

    @classmethod
    def initialize(cls):
        Lands.initialize()
        Players.initialize()


    @classmethod
    def new_match(cls):
        Players.first_conditions()
        Lands.first_conditions()

    @classmethod
    def sort_players(cls):
        sorted_players = Players.sorted_players()
        return sorted_players

    @classmethod
    def save_round_results(cls, game_round, id_winner, timeout):
        OutputSimulation.update_results(game_round, id_winner, timeout)

    @classmethod
    def check_if_round_continue(cls):
        round_continue = True
        id_winner = None
        players = Players.get_players()
        count = 0
        balance = 0
        for player in players:
            if player['activate']==0:
                count = count + 1
            if count == TOTAL_PLAYERS-1:
                # Return winner
                round_continue = False
                id_winner = player['id']
                return round_continue, id_winner

            if round_continue==True:
                if player['balance_value']>balance:
                    balance = player['balance_value']
                    id_winner = player['id']

        if round_continue == True:
                # return winner by timeout
                pass

        return round_continue, id_winner

    @classmethod
    def buy_land_if_wish(cls, board_position, id_player):
        if Players.buy_or_not(board_position, id_player):
            player = Players.get_player(id_player)
            land = Lands.get_land(board_position)

            # Update player
            player['balance_value'] = player['balance_value'] - land['sale_value']
            if player['balance_value']<=0:
                player['activate']=0

            Players.update_player(id_player, player)

            # Update land
            land['owner'] = id_player
            Lands.update_land(board_position, land)
        else:
            pass

    @classmethod
    def pay_land(cls, board_position, id_player):
        player = Players.get_player(id_player)
        land = Lands.get_land(board_position)

        # Update player
        player['balance_value'] = player['balance_value'] - land['rent_value']
        if player['balance_value'] <= 0:
            player['activate'] = 0

            # Update land
            land['owner'] = None
            Lands.update_land(board_position, land)
        Players.update_player(id_player, player)

    @classmethod
    def play(cls, timeout, sorted_players):
        game_round = 1
        id_winner = None
        while game_round <= timeout:
            for player in sorted_players:
                activate_player = Players.get_player(player)['activate']
                if activate_player ==0:
                    pass
                else:
                    board_position = Players.move_to(player)

                    if Lands.check_land_is_available(board_position) is True:
                        cls.buy_land_if_wish(board_position, player)
                    else:
                        cls.pay_land(board_position, player)

            check_round, id_winner = BankGame.check_if_round_continue()
            if check_round:
                pass
            else:
                break
            game_round += 1

        cls.save_round_results(game_round, id_winner, timeout)