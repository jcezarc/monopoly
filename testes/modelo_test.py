from util.testador import Testador
from modelo.comportamento import (
    Cauteloso,
    Exigente,
    Impulsivo
)


def test_recusa_compra():
    '''
    Simula a decisão de comprar uma casa,
    deixando de saldo apenas $ 20.
    Mas o comportamento Cauteloso não permite
    que o saldo fique abaixo de $80.
    '''
    ambiente = Testador([Cauteloso])
    jogador = ambiente.jogador1()
    casa = ambiente.casa(0)
    # Comprar essa casa deixaria só $20 de saldo:
    casa.custo_venda = jogador.saldo - 20
    assert not jogador.decide_compra(casa)


def test_compra_vantajosa():
    '''
    Simula a decisão de comprar uma casa,
    cujo aluguel está acima do rendimento
    esperado pelo comportamento Exigente.
    '''
    ambiente = Testador([Exigente])
    jogador = ambiente.jogador1()
    casa = ambiente.casa(0)
    casa.valor_aluguel = 75
    assert jogador.decide_compra(casa)


def test_gastador():
    '''
    Faz a compra de várias casas
    até ficar sem saldo suficiente.
    '''
    ambiente = Testador([Impulsivo])
    jogador = ambiente.jogador1()
    jogador.saldo = 500
    # Com esse saldo ele pode comprar 3 casas de 160:
    compras = 0
    for casa in ambiente.jogo.tabuleiro:
        casa.custo_venda = 160
        if jogador.decide_compra(casa):
            jogador.realiza_compra(casa)
            compras += 1
        else:
            break
    assert compras == 3
    assert jogador.saldo == 20
