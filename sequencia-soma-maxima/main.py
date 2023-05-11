import sequencia_soma_maxima as SequenciaSomaMaxima
import sequencia_soma_maxima_v2 as SequenciaSomaMaximaV2

arranjo = [-2, 11, -4, 13, -5, 2]
(inicio, fim, soma) = SequenciaSomaMaxima.encontre_sequencia_soma_maxima(arranjo)
(inicio2, fim2, soma2) = SequenciaSomaMaximaV2.encontre_sequencia_soma_maxima(arranjo)
print(f'Entrada: {arranjo}\n== Sequência soma máxima (v1) ==\n' \
  f'Soma máxima: {soma}, início: {inicio}, fim: {fim}\n' \
  f'Subsequência de soma máxima: {arranjo[inicio:fim + 1]}'\
  f'\n== Sequência soma máxima (v2) ==\n' \
  f'Soma máxima: {soma2}, início: {inicio2}, fim: {fim2}\n' \
  f'Subsequência de soma máxima: {arranjo[inicio2:fim2 + 1]}')
  