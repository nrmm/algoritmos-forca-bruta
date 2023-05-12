import math
import itertools

def encontre_itens(valores, pesos, capacidade):
    n = len(valores)
    soma_maxima = -math.inf
    itens = ()
    for i in range(1, n):
        for combinacao in itertools.combinations(range(n), i):
            soma_valores = 0
            capacidade_utilizada = 0
            for item in combinacao:
                soma_valores += valores[item]
                capacidade_utilizada += pesos[item]
            if soma_valores > soma_maxima and capacidade_utilizada <= capacidade:
                itens = combinacao
                soma_maxima = soma_valores
    return (itens, soma_maxima)
