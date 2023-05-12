import grafo_matriz_adjacencia as Grafo
import caixeiro_viajante as Caixeiro

# Grafo completo K-4.
grafo = Grafo.GrafoMatrizAdjacencia(4)
grafo.adicione_aresta(0, 1, 2)
grafo.adicione_aresta(0, 2, 5)
grafo.adicione_aresta(0, 3, 7)
grafo.adicione_aresta(1, 2, 8)
grafo.adicione_aresta(1, 3, 3)
grafo.adicione_aresta(2, 3, 1)
grafo.imprima_grafo()
(ciclo, custo) = Caixeiro.encontre_ciclo_hamiltoniano_com_custo_minimo(grafo, 0)
print(f'Ciclo hamiltoniano c/ custo mínimo: {ciclo}\nCusto: {custo}')
