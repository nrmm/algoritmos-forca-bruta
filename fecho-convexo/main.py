import fecho_convexo as FechoConvexo

pontos = [(1,1), (2,4), (3,1), (5,1), (2,-3), (4,1), (2,2)]
fecho = FechoConvexo.encontre_fecho_convexo(pontos)
print(f'Conjunto de pontos de entrada: {pontos}\nFecho convexo: {fecho}')