import logging

logging.basicConfig(level=logging.INFO, filename='banco_imobiliario.log')

MAIS_SALDO = '\n\t\tSaldo: {:.2f} + {:.2f} = {:.2f}'
MAIS_SALDO_DE = MAIS_SALDO.replace('Saldo:', '{}:')
MENOS_SALDO = '\n\t\tSaldo: {:.2f} - {:.2f} = {:.2f}'


class Marcador:
    '''
        Faz os registros de todos os acontecimentos no jogo
        É usada como um decorator nos métodos das 
        classes Jogo, Jogador e Propriedade
    '''

    @staticmethod
    def cobra_aluguel(func):
        def wrapper(*args, **kw):
            casa = args[0]
            jogador = args[1]
            logging.info('\t(-) {} paga aluguel da casa {} para {}{}{}'.format(
                jogador.nome,
                casa.endereco+1,
                casa.dono.nome,
                MENOS_SALDO.format(
                    jogador.saldo, casa.valor_aluguel,
                    jogador.saldo - casa.valor_aluguel,
                ),
                MAIS_SALDO_DE.format( 
                    casa.dono.nome,
                    casa.dono.saldo, casa.valor_aluguel,
                    casa.dono.saldo + casa.valor_aluguel,
                )
            ))
            return func(*args, **kw)
        return wrapper

    @staticmethod
    def realiza_compra(func):
        def wrapper(*args, **kw):
            jogador = args[0]
            casa = args[1]
            logging.info('\t[+] Casa {} vendida para {}{}'.format(
                casa.endereco+1,
                jogador.nome,
                MENOS_SALDO.format(
                    jogador.saldo, casa.custo_venda,
                    jogador.saldo - casa.custo_venda,
                )
            ))
            return func(*args, **kw)
        return wrapper

    @staticmethod
    def proxima_rodada(func):
        def wrapper(*args, **kw):
            jogo = args[0]
            if len(args) > 1:
                numero_jogo = args[1]
                logging.info('{} JOGO {} {}'.format(
                    '='*50,
                    numero_jogo,
                    '='*50,
            ))
            func(*args, **kw)
            logging.info('--------- Rodada {} ------------'.format(jogo.rodada))
        return wrapper

    @staticmethod
    def fim_de_jogo(func):
        def wrapper(*args, **kw):
            jogo = args[0]
            motivo = args[1]
            func(*args, **kw)
            vencedor = jogo.vencedor
            logging.info('\t</> ***** Fim de jogo \t\t{} venceu por {}\t{}'.format(
                vencedor.nome,
                motivo,
                '_'*20
            ))
            return vencedor
        return wrapper

    @staticmethod
    def remove_jogador(func):
        def wrapper(*args, **kw):
            perdedor = args[1]
            logging.info('\t{!}'+'Jogador {} removido do jogo.'.format(
                perdedor.nome
            ))
            func(*args, **kw)
        return wrapper

    @staticmethod
    def ganha_bonus(func):
        def wrapper(*args, **kw):
            jogador = args[0]
            valor = args[1]
            logging.info('\t @  {} completou +1 volta{}'.format(
                jogador.nome,
                MAIS_SALDO.format(
                    jogador.saldo, valor,
                    jogador.saldo + valor,
                )
            ))
            func(*args, **kw)
        return wrapper
