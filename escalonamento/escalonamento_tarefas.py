import math
import itertools

def encontre_escalonamento_minimo(custos):
    n = len(custos[0])
    custo_minimo = math.inf
    escalonamento_minimo = ()
    for permutacao in itertools.permutations(range(n), n):
        soma = 0
        for i in range(n):
            soma += custos[i][permutacao[i]]
        if soma < custo_minimo:
            custo_minimo = soma
            escalonamento_minimo = permutacao
    return escalonamento_minimo, custo_minimo
