import json
from collections import defaultdict

with open("datos/ejercicio2_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
inicio = datos["inicio"]
objetivo = datos["objetivo"]

def contar_intermedios(grafo, inicio, objetivo):
    conteo = defaultdict(int)

    def dfs(nodo, camino):
        if nodo == objetivo:
            for intermedio in set(camino[1:-1]):
                conteo[intermedio] += 1
            return
        for vecino in grafo.get(nodo, {}):
            if vecino not in camino:
                dfs(vecino, camino + [vecino])

    dfs(inicio, [inicio])
    return dict(conteo)

print(contar_intermedios(grafo, inicio, objetivo))

