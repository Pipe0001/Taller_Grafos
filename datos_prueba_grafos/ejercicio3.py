from Datos.ejercicio3_datos import grafo

edges = []
for u in grafo:
    for v, w in grafo[u]:
        if (v, u, w) not in edges:
            edges.append((u, v, w))
edges.sort(key=lambda x: x[2])

parent = {n: n for n in grafo}
def find(n):
    while parent[n] != n:
        parent[n] = parent[parent[n]]
        n = parent[n]
    return n

def union(u, v):
    ru, rv = find(u), find(v)
    if ru != rv:
        parent[rv] = ru
        return True
    return False

mst, total = [], 0
for u, v, w in edges:
    if union(u, v):
        mst.append((u, v, w))
        total += w

print("MST:", mst)
print("Costo total:", total)
