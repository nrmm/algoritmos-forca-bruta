def encontre_fecho_convexo(pontos):
    hull = set()
    for pi in range(len(pontos) - 1):
        for pj in range(pi + 1, len(pontos)):
            x1, y1 = pontos[pi]
            x2, y2 = pontos[pj]
            a = y2 - y1
            b = x1 - x2
            c = x1 * y2 - x2 * y1
            possui_negativos = False
            possui_positivos = False
            for i in range(len(pontos)):
                # Ignora pontos da própria reta.
                if pontos[i] == (x1, y1) or pontos[i] == (x2, y2):
                    continue
                p = pontos[i]
                resultado = a * p[0] + b * p[1] - c
                if resultado >= 0:
                    possui_positivos = True
                else:
                    possui_negativos = True
            # Verifica se os pontos são externos.
            if possui_positivos and not possui_negativos or not possui_positivos and possui_negativos:
                hull.add((x1, y1))
                hull.add((x2, y2))
    return hull
