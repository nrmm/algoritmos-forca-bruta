def ordene(arranjo):
    """Implementação da ordenação por seleção.
    Operação básica: comparação.
    Complexidade: O(n^2) nos 3 cenários de execução:
    melhor caso, caso médio e pior caso.
    """
    n = len(arranjo)
    for i in range(n - 2):
        min = i
        for j in range(i + 1, n):
            if arranjo[j] < arranjo[min]:
                min = j
        tmp = arranjo[i]
        arranjo[i] = arranjo[min]
        arranjo[min] = tmp
