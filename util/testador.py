from util.gera_numeros import ativa_testes
import logging
from modelo.comportamento import Impulsivo, Aleatorio
from regra.jogo import Jogo
import sys

sys.path.append('.')
sys.path.append('..')


class Testador:

    """
    Responsável pelos dados de teste
    """
    def __init__(self, tipos_jogadores=[Impulsivo, Aleatorio]):
        logging.info('####### Iniciando TESTES ############')
        ativa_testes()
        self.jogo = Jogo(
            0,  # número do jogo
            casas_tabuleiro=10,
            tipos_jogadores=tipos_jogadores,
            limite_rodadas=50
        )

    def jogador1(self):
        return self.jogo.jogadores_ativos[0]
        # James Halliday, Samantha Cook, Helen Harris, Daito, Wade Watts

    def casa(self, endereco):
        return self.jogo.tabuleiro[endereco]

    def vencedor_esperado(self, jogador):
        return self.jogo.vencedor == jogador
