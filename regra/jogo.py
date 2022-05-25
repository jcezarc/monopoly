from itertools import cycle
from util.gera_numeros import CLASSE_NUMEROS
from saida.marcador import Marcador
from modelo.comportamento import (
    Impulsivo,
    Exigente,
    Cauteloso,
    Aleatorio
)
from regra.item import Propriedade, Jogador


class Jogo:

    @Marcador.proxima_rodada
    def __init__(self, numero, **kw):
        """
        Cria o tabuleiro e
        Também cria 4 jogadores,
        um de cada comportamento

        :numero - identifia o jogo no decorator
        """
        casas_tabuleiro = kw.get('casas_tabuleiro', 20)
        tipos_jogadores = kw.get('tipos_jogadores', [
            Impulsivo,
            Exigente,
            Cauteloso,
            Aleatorio
        ])
        self.tabuleiro = Propriedade.fabrica(
            range(casas_tabuleiro)
        )
        self.jogadores_ativos = Jogador.fabrica(tipos_jogadores)
        self.rodada = 1
        self.motivo = ''
        self.sequencia_jogo = cycle(self.jogadores_ativos)
        self.limite_rodadas = kw.get('limite_rodadas', 100)
        self.vencedor = None

    def __jogador_atual(self):
        return next(self.sequencia_jogo)

    @Marcador.proxima_rodada
    def proxima_rodada(self):
        self.rodada += 1

    def executa(self):
        if not self.jogadores_ativos:
            raise Exception('Nenhum jogador ativo')
        jogador = self.__jogador_atual()
        jogador.movimenta(CLASSE_NUMEROS.lanca_dados(), self.tabuleiro)
        if jogador.saldo < 0:
            self.remove_jogador(jogador)
        if len(self.jogadores_ativos) == 1:
            self.fim_de_jogo('WO')
            return False
            #      ^^^---- vitória por W.O.
        if jogador == self.jogadores_ativos[-1]:
            self.proxima_rodada()
            if self.rodada >= self.limite_rodadas:
                self.fim_de_jogo('TimeOut')
                return False
        return True

    @Marcador.remove_jogador
    def remove_jogador(self, perdedor):
        while perdedor.imoveis:
            casa = perdedor.imoveis.pop()
            casa.dono = None
        self.jogadores_ativos.remove(perdedor)
        self.sequencia_jogo = cycle(self.jogadores_ativos)

    @Marcador.fim_de_jogo
    def fim_de_jogo(self, motivo):
        """
        `jogadores_ativos` está em ordem de turno
        portanto o primeiro a ser aclamado vencedor
        tem precedência sobre outro com saldo empatado.
        """
        vencedor = None
        for jogador in self.jogadores_ativos:
            if not vencedor or jogador.saldo > vencedor.saldo:
                vencedor = jogador
        self.motivo = motivo
        self.vencedor = vencedor
