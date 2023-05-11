def pesquise(chave, arranjo):
    """Implementação da busca sequencial para entradas ordenadas.
    A otimização consiste em abortar a pesquisa caso seja encontrado
    registro com chave maior do que a do elemento procurado.
    Operação básica: comparação.
    Complexidade:
      - melhor caso: O(1), chave na posição inicial;
      - caso médio e pior caso: O(n).
    """
    for i in range(len(arranjo)):
        if arranjo[i] == chave:
            return i
        elif arranjo[i] > chave:
            return -1
    return -1
