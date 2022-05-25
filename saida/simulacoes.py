from collections import Counter

DEFAULT_QT_JOGOS = 300
MAX_RODADAS = 1000


class Simulacao:
    def __init__(self):
        self.partidas = Counter()
        self.vitorias = Counter()
        self.turnos = 0
        self.total = 0

    def nova_partida(self, jogo):
        while jogo.executa():
            self.turnos += 1
        self.partidas[jogo.motivo] += 1
        tipo_jogador = jogo.vencedor.nome
        self.vitorias[tipo_jogador] += 1
        self.total += 1

    def media_turnos(self):
        return self.turnos / self.total

    def melhor_jogador(self):
        melhor, resumo = None, []
        for tipo, contagem in self.vitorias.items():
            porcentagem = contagem / self.total * 100
            if not melhor or contagem > self.vitorias[melhor]:
                melhor = tipo
            resumo.append('\t\t {} = {:.2f} %'.format(
                tipo.rjust(10),
                porcentagem
            ))
        return melhor, resumo


def roda_simulacoes(classe_jogo, qt_jogos=DEFAULT_QT_JOGOS):
    """
    Roda as simulações do jogo conforme parametros
    ...
    :classe_jogo = Objeto-jogo deve ser instanciado
                em cada simulação
    :qt_jogos = Quantos jogos devem ser executados
    """
    simulacao = Simulacao()
    for i in range(1, qt_jogos+1):
        jogo = classe_jogo(i, limite_rodadas=MAX_RODADAS)
        simulacao.nova_partida(jogo)
    mostra_resumo(simulacao)


def mostra_resumo(simulacao):
    print('='*50)
    print('::::::::: RESUMO E ESTATISTICAS :::::::::')
    print('-'*50)
    print('\tTotal de partidas = {}'.format(simulacao.total))
    print(
        '\tPartidas que terminaram em Time Out = ',
        simulacao.partidas['TimeOut']
    )
    print('\tMedia de turnos = {:.2f}'.format(simulacao.media_turnos()))
    print('\tVitorias por tipo:')
    melhor, resumo = simulacao.melhor_jogador()
    for linha in resumo:
        print(linha)
    print('\tTipo que mais venceu = ', melhor)
    print('-'*50)
