def ordene(arranjo):
    """Implementação ingênua do BubbleSort.
    Operação básica: comparação.
    Complexidade: O(n^2) nos 3 cenários de execução:
    melhor caso, caso médio e pior caso.
    """
    n = len(arranjo)
    for i in range(n - 2):
        for j in range(n - i - 2):
            if arranjo[j] > arranjo[j + 1]:
                tmp = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = tmp
