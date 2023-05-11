import math

def encontre_sequencia_soma_maxima(arranjo):
    soma_maxima = -math.inf
    inicio = fim = 0
    n = len(arranjo)
    for i in range(n):
        soma = 0
        for j in range(i, n):
            soma += arranjo[j]
            if soma > soma_maxima:
                soma_maxima = soma
                inicio = i
                fim = j
    return (inicio, fim, soma_maxima)
