def pesquise(chave, arranjo):
    """Implementação da busca sequencial com inclusão de sentinela.
    A otimização consiste em eliminar a comparação referente ao tamanho
    do arranjo.
    Operação básica: comparação.
    Complexidade:
      - melhor caso: O(1), chave na posição inicial;
      - caso médio e pior caso: O(n).
    """
    arranjo.append(chave)
    i = 0
    while arranjo[i] != chave:
        i += 1
    arranjo.pop()
    return i
