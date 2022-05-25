from modelo.comportamento import Aleatorio, Avarento
from util.testador import Testador


def test_aluguel():
    """
    Dados dois jogadores, um deles dono de uma casa,
    testa como cobrar aluguel afeta o saldo de ambos.
    """
    ambiente = Testador([Aleatorio, Aleatorio])
    jogador, adversario = ambiente.jogo.jogadores_ativos
    jogador.saldo = 300
    # ---------------------
    casa = ambiente.casa(3)
    casa.custo_venda = 175
    casa.valor_aluguel = 90
    # ---------------------
    adversario.saldo = 300
    adversario.realiza_compra(casa)
    # ---------------------
    casa.cobra_aluguel(jogador)
    assert adversario.saldo == 215  # 300 - 175 + 90
    assert jogador.saldo == 210  # 300 - 90


def test_bonus():
    ambiente = Testador([Avarento])
    jogador = ambiente.jogador1()
    jogador.saldo = 300
    jogador.movimenta(11, ambiente.jogo.tabuleiro)
    assert jogador.saldo == 400
