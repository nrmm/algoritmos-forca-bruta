import busca_sequencial as BuscaSequencial
import busca_sequencial_v2 as BuscaSequencialV2
import busca_sequencial_v3 as BuscaSequencialV3

arranjo = [27, 30, 42, 9, -1, -5]
chave = 9
pos = BuscaSequencial.pesquise(chave, arranjo)
pos2 = BuscaSequencialV2.pesquise(chave, arranjo)
arranjo.sort()
pos3 = BuscaSequencialV3.pesquise(chave, arranjo)
print(f'Entrada: {arranjo}\nValor de pesquisa: {chave}\n' \
  f'Índice do valor de pesquisa (busca v1): {pos}\n' \
  f'Índice do valor de pesquisa (busca v2): {pos2}\n' \
  f'Índice do valor de pesquisa (busca v3): {pos3}')
