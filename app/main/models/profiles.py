from app.main.models.lands import LandModel
from app.main.models.players import PlayerModel
import random





class PlayersProfiles:
    def __init__(self,  board_position, id_player):
        self.board_position =  board_position
        self.id_player = id_player
        self.land = LandModel.read_lands(self.board_position)


    def type_1(self):
        """ O jogador impulsivo compra qualquer propriedade sobre a qual ele parar. """
        return True


    def type_2(self):
        """ O jogador exigente compra qualquer propriedade, desde que o valor do aluguel
            ela seja maior do que 50. """
        # print('ran_value', self.land['rent_value'] )

        if self.land['rent_value'] >50:
            return True
        else:
            return False


    def type_3(self):
        """ O jogador cauteloso compra qualquer propriedade desde que ele tenha uma reserva de 80 saldo sobrando
            depois de realizada a compra."""

        balance_value = PlayerModel.read_player(self.id_player)['balance_value']
        residual =  balance_value - self.land['sale_value']
        if residual >= 80:
            return True
        else:
            return False

    def type_4(self):
        """ O jogador aleatório compra a propriedade que ele parar em cima com probabilidade de 50%. """
        return bool(random.getrandbits(1))

    def buy_according_profile(self):
        profiles = {
            1: self.type_1(),
            2: self.type_2(),
            3: self.type_3(),
            4: self.type_4()
        }
        return profiles[self.id_player]