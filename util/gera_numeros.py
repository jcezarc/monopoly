import random

class NumerosAleatorios:
    @staticmethod
    def lanca_dados():
        return random.randint(1,6)

    @staticmethod
    def true_ou_false():
        return bool(random.getrandbits(1))

    @staticmethod
    def embaralha(lista):
        random.shuffle(lista)
        return lista

    @staticmethod
    def valor(minimo, maximo):
        return random.randrange(minimo, maximo)


class NumerosParaTeste:
    @staticmethod
    def lanca_dados():
        return 1

    @staticmethod
    def true_ou_false():
        return True

    @staticmethod
    def embaralha(lista):
        return lista

    @staticmethod
    def valor(minimo, maximo):
        return (minimo+maximo)/2


CLASSE_NUMEROS = NumerosAleatorios



def ativa_testes():
    # global CLASSE_NUMEROS
    # CLASSE_NUMEROS = NumerosParaTeste
    c1, c2 = NumerosAleatorios, NumerosParaTeste
    c1.lanca_dados = c2.lanca_dados
    c1.true_ou_false = c2.true_ou_false
    c1.embaralha = c2.embaralha
    c1.valor = c2.valor
