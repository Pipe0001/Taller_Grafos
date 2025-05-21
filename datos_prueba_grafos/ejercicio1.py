import json
import heapq

with open("datos/ejercicio1_datos.json") as f:
    datos = json.load(f)

grafo = datos["grafo"]
origen = datos["origen"]
destino = datos["destino"]

def dijkstra(grafo, origen, destino):
    heap = [(0, origen, [])]
    visitados = set()

    while heap:
        costo, nodo, camino = heapq.heappop(heap)
        if nodo in visitados:
            continue
        camino = camino + [nodo]
        if nodo == destino:
            return camino, costo
        visitados.add(nodo)
        for vecino, peso in grafo[nodo].items():
            heapq.heappush(heap, (costo + peso, vecino, camino))
    return [], float('inf')

camino, costo = dijkstra(grafo, origen, destino)
print("Camino más corto:", camino)
print("Costo total:", costo)
