import par_mais_proximo as ParMaisProximo

pontos = [(1,1), (2,-3), (2,4)]
(inicio, fim, distancia) = ParMaisProximo.encontre_par_mais_proximo(pontos)
print(f'Entrada: {pontos}\nDistância mínima: {distancia},' \
  f' Pontos: ({pontos[inicio][0]},{pontos[inicio][1]}) e ' \
  f'({pontos[fim][0]},{pontos[fim][1]})')
  