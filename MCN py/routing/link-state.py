n = int(input("Enter number of nodes: "))
print("Enter cost matrix (row by row, use 9999 for infinity):")
cost = [list(map(int, input().split())) for _ in range(n)]
src = int(input("Enter source node: "))

dist = cost[src][:]
visited = [False] * n
visited[src] = True

for _ in range(n - 1):
    u = min((i for i in range(n) if not visited[i]), key=lambda i: dist[i])
    visited[u] = True
    
    for v in range(n):
        if not visited[v] and cost[u][v] != 9999:
            dist[v] = min(dist[v], dist[u] + cost[u][v])

print(f"Shortest distances from node {src}: {dist}")