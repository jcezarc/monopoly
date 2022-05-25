from util.gera_numeros import CLASSE_NUMEROS

'''
Cada comportamento é definido
por um conjunto de condições que
podem ser combinadas com outras.

Ex.:
condicoes_combinadas = Cauteloso.condicoes() + Exigente.condicoes()
'''

CONDICAO_PADRAO = lambda propriedade, jogador: jogador.saldo >= propriedade.custo_venda


class Impulsivo:
    def condicoes(self):
        return [CONDICAO_PADRAO]


class Exigente:
    def condicoes(self):
        return [CONDICAO_PADRAO,
            lambda propriedade, jogador: propriedade.valor_aluguel > 50
        ]


class Cauteloso:
    def condicoes(self):
        return [
            lambda propriedade, jogador: jogador.saldo - propriedade.custo_venda >= 80
        ]


class Aleatorio:
    def condicoes(self):
        return [CONDICAO_PADRAO,
            lambda propriedade, jogador: CLASSE_NUMEROS.true_ou_false()
        ]

# ---- Somente para testes ----
class Avarento:
        def condicoes(self):
            return [
                lambda propriedade, jogador: False
            ]
