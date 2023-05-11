import casamento_exato as CasamentoExato

texto = "foothe lazy fox jumped over the brown dogbar"
padrao = "foobar"
indice = CasamentoExato.casamento(texto, padrao)
print(f'Entrada: \"{texto}\"\nPadrão: \"{padrao}\"\nÍndice: {indice}')
