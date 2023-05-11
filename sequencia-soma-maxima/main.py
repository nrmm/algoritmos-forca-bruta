import sequencia_soma_maxima as SequenciaSomaMaxima

arranjo = [-2, 11, -4, 13, -5, 2]
(inicio, fim, soma) = SequenciaSomaMaxima.encontre_sequencia_soma_maxima(arranjo)
print(f'Entrada: {arranjo}\nSoma máxima: {soma}, ' \
  f'início: {inicio}, fim: {fim}\n' \
  f'Subsequência de soma máxima: {arranjo[inicio:fim + 1]}')
  