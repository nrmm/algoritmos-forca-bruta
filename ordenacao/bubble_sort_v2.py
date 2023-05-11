def ordene(arranjo):
    """Implementação do BubbleSort com uma pequena otimização, referente
    a entrada já ordenada.
    Operação básica: comparação.
    - Melhor caso: O(n);
    - Caso médio e pior caso: O(n^2).
    """
    n = len(arranjo)
    for i in range(n - 2):
        houve_troca = False
        for j in range(n - i - 2):
            if arranjo[j] > arranjo[j + 1]:
                houve_troca = True
                tmp = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = tmp
        if not houve_troca:
            break
