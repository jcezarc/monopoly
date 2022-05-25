from modelo.comportamento import Avarento, Impulsivo
from util.testador import Testador
from saida.simulacoes import Simulacao, mostra_resumo


def test_rodadas():
    """
    Simula que se passaram 4 rodadas
    """
    jogo = Testador([Avarento]).jogo
    for _ in range(4):
        jogo.proxima_rodada()
    assert jogo.rodada == 5


def test_jogador_removido():
    """
    Quando o jogador é removido do jogo,
    todas as suas propriedades ficam sem dono
    """
    ambiente = Testador([Impulsivo])
    jogador = ambiente.jogador1()
    jogador.saldo = 1000
    for casa in ambiente.jogo.tabuleiro[:5]:
        casa.custo_venda = 200
        jogador.realiza_compra(casa)
    assert len(jogador.imoveis) == 5
    ambiente.jogo.remove_jogador(jogador)
    assert not jogador.imoveis
    tabuleiro = ambiente.jogo.tabuleiro
    assert not any(casa.dono for casa in tabuleiro)


def test_tudo_junto():
    """
    Combina várias coisas na rotina
    do jogo: movimentar o jogador,
    eliminar jogadores sem saldo e verificar
    se o jogo terminou
    """
    ambiente = Testador([Impulsivo, Avarento])
    jogador, adversario = ambiente.jogo.jogadores_ativos
    simulacao = Simulacao()
    simulacao.nova_partida(ambiente.jogo)
    assert ambiente.vencedor_esperado(jogador)
    return simulacao


if __name__ == '__main__':
    mostra_resumo(
        test_tudo_junto()
    )
