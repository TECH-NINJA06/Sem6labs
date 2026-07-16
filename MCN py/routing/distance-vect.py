V, E = map(int, input("Enter number of Vertices and Edges: ").split())
print("Enter edges (source dest weight):")
edges = [list(map(int, input().split())) for _ in range(E)]
src = int(input("Enter source node: "))

dist = [9999] * V
dist[src] = 0

for _ in range(V - 1):
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

print(f"Distance Vector from node {src}: {dist}")