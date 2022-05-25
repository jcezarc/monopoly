from util.gera_numeros import CLASSE_NUMEROS
from saida.marcador import Marcador


class FabricaItens:

    @classmethod
    def fabrica(cls, dados):
        """
        Disponibiliza um lote de itens
        `fabricados` através dos dados recebidos.
        """
        if isinstance(dados, list):
            CLASSE_NUMEROS.embaralha(dados)
        return [cls(info) for info in dados]    


class Propriedade(FabricaItens):
    '''
    Classe que representa um imóvel (ou `casa`)
    numa *posição* do tabuleiro
    
    :endereco: Posição do imóvel no tabuleiro
    '''
    def __init__(self, endereco):
        self.endereco = endereco
        self.custo_venda = CLASSE_NUMEROS.valor(100, 200)
        self.valor_aluguel = CLASSE_NUMEROS.valor(30, 90)
        self.dono = None
        
    @Marcador.cobra_aluguel
    def cobra_aluguel(self, jogador):
        jogador.saldo -= self.valor_aluguel
        self.dono.saldo += self.valor_aluguel


class Jogador(FabricaItens):
    """
    `Jogador` é um elemento que age
    dentro do jogo se movimentando pelas
    casas do tabuleiro.

    :comportamento: é *injetado* por alguma
    classe modelo.comportamento e determina
    quando o jogador deve comprar uma casa.
    """
    def __init__(self, classe_comportamento):
        self.comportamento = classe_comportamento()
        self.nome = self.comportamento.__class__.__name__
        self.saldo = 300
        self.posicao = 0
        self.imoveis = []

    @Marcador.realiza_compra
    def realiza_compra(self, propriedade):
        self.saldo -= propriedade.custo_venda
        propriedade.dono = self
        self.imoveis.append(propriedade)
    
    def decide_compra(self, propriedade):
        return all(
            func(propriedade, self) 
            for func in self.comportamento.condicoes()
        )

    @Marcador.ganha_bonus
    def ganha_bonus(self, valor):
        self.saldo += valor

    def movimenta(self, distancia, tabuleiro):
        """
        Aqui `casa` também é uma Propriedade,
        mas é tratada como um espaço no tabuleiro
        """
        destino = self.posicao + distancia
        qt_casas = len(tabuleiro)
        if destino >= qt_casas:
            self.ganha_bonus(100) #--- Completou uma volta!
            destino %= qt_casas
        casa = tabuleiro[destino]
        if casa.dono:
            if casa.dono != self:
                casa.cobra_aluguel(self)
        elif self.decide_compra(casa):
            self.realiza_compra(casa)
        self.posicao = destino
