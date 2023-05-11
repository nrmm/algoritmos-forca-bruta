def casamento(texto, padrao):
    """Implementação ingênua do algoritmo para encontrar casamento de cadeias.
    Operação básica: comparação.
    Complexidade:
      - melhor caso: O(m)
      - pior caso: O(mn)
    """
    n = len(texto)
    m = len(padrao)
    for i in range(n - m):
        j = 0
        while j < m and texto[i + j] == padrao[j]:
            j += 1
        # Padrão encontrado no texto.
        if j == m:
            return i
    return -1
