def pesquise(chave, arranjo):
    """Implementação ingênua da busca sequencial.
    Operação básica: comparação.
    Complexidade:
      - melhor caso: O(1), chave na posição inicial;
      - caso médio e pior caso: O(n).
    """
    for i in range(len(arranjo)):
        if arranjo[i] == chave:
            return i
    return -1
