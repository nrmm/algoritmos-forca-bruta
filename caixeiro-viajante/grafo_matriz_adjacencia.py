class GrafoMatrizAdjacencia:
    def __init__(self, qtde_vertices):
        self.qtde_vertices = qtde_vertices
        self.matriz = [[0] * qtde_vertices for i in range(qtde_vertices)]
        self.custo_operacao_basica = self.qtde_vertices

    def adicione_aresta(self, u, v, peso=1):
            self.matriz[u][v] = peso
            self.matriz[v][u] = peso

    def remova_aresta(self, u, v):
        self.matriz[u][v] = 0
        self.matriz[v][u] = 0

    # FIXME: ajustar para arestas com peso.
    def grau(self, v):
        grau = 0
        for i in range(self.qtde_vertices):
            grau += self.matriz[v][i]
        return grau

    def numero_vertices(self):
        return self.qtde_vertices

    def numero_arestas(self):
        somatorio_graus = 0
        for v in range(self.qtde_vertices):
            somatorio_graus += self.grau(v)
        return somatorio_graus // 2

    def peso(self, u, v):
        return self.matriz[u][v]

    def adjacente(self, u, v):
        return self.matriz[u][v] > 0
    
    def vertices_adjacentes(self, v):
        return [i for i in range(self.qtde_vertices) if self.adjacente(v, i)]

    def possui_loop(self):
        for i in range(self.qtde_vertices):
            if self.matriz[i][i] != 0:
                return True
        return False
    
    def possui_arestas_paralelas(self):
        for i in range(self.qtde_vertices):
            for j in range(self.qtde_vertices):
                if self.matriz[i][j] > 1:
                    return True
        return False
    
    def possui_vertice_grau_impar(self):
        for i in range(self.qtde_vertices):
            if (self.grau(i) % 2 != 0):
                return True
        return False
    
    def imprima_grafo(self):
        for i in range(self.qtde_vertices):
            print("Vértice", i, ":", end=" ")
            for j in range(self.qtde_vertices):
                print(self.matriz[i][j], end=" ")
            print()
