import math
import itertools

def encontre_ciclo_hamiltoniano_com_custo_minimo(grafo, vertice_inicial):
    custo_minimo = math.inf
    ciclo_com_custo_minimo = ()
    n = grafo.numero_vertices()
    conjunto_vertices = list(range(n))
    # Remove vértice inicial, pois as permutações são geradas apenas
    # para os vértices intermediários.
    del conjunto_vertices[vertice_inicial]
    for permutacao in itertools.permutations(conjunto_vertices, n - 1):
        ciclo = (vertice_inicial,) + permutacao + (vertice_inicial,)
        custo = 0
        # Verifica adjacências.
        for i in range(len(ciclo) - 1):
            u = ciclo[i]
            v = ciclo[i + 1]
            if grafo.adjacente(u, v):
                custo += grafo.peso(u, v)
            # Caso u-v não sejam adjacentes, não há ciclo.
            else:
                custo = math.inf
                break
        if custo < custo_minimo:
            custo_minimo = custo
            ciclo_com_custo_minimo = ciclo
    return (ciclo_com_custo_minimo, custo_minimo)
