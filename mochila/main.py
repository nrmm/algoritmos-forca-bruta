import mochila as Mochila

valor_itens = [42, 12, 40, 25]
peso_itens = [7, 3, 4, 5]
capacidade = 10
(itens, soma_maxima) = Mochila.encontre_itens(valor_itens, peso_itens, capacidade)
print(f'Valor dos itens: {valor_itens}\nPeso dos itens: {peso_itens}\n' \
  f'Capacidade da mochila: {capacidade}\nSoma máxima: {soma_maxima}\n' \
  f'Itens a serem escolhidos: {itens}')
  