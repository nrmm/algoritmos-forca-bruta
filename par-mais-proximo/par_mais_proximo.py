import math

def encontre_par_mais_proximo(pontos):
    """Encontra o par de pontos com a menor distância.
    Operação básica: comparação.
    Complexidade: O(n^2) para os 3 cenários de execução:
    melhor caso, caso médio e pior caso.
    """
    n = len(pontos)
    inicio = fim = 0
    distancia_minima = math.inf
    for i in range(n - 1):
        for j in range(i + 1, n):
            (x1, y1) = pontos[i]
            (x2, y2) = pontos[j]
            dx = x1 - x2
            dy = y1 - y2
            distancia = math.sqrt(dx**2 + dy**2)
            if distancia < distancia_minima:
                distancia_minima = distancia
                inicio = i
                fim = j
    return (inicio, fim, distancia_minima)
