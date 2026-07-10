#include <iostream>
using namespace std;

struct Edge {
    int u, v, w;
};

int main() {
    int V, E, src;
    
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    Edge edges[E];
    cout << "Enter edges (source destination weight):\n";
    for (int i = 0; i < E; i++) {
        cin >> edges[i].u >> edges[i].v >> edges[i].w;
    }

    cout << "Enter source node: ";
    cin >> src;

    int dist[V];
    for (int i = 0; i < V; i++) {
        dist[i] = 9999; 
    }
    dist[src] = 0;

    for (int i = 1; i <= V - 1; i++) {
        for (int j = 0; j < E; j++) {
            int u = edges[j].u;
            int v = edges[j].v;
            int w = edges[j].w;
            if (dist[u] != 9999 && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    cout << "\nDistance Vector Routing Table for Node " << src << ":\n";
    cout << "Destination\tDistance\n";
    for (int i = 0; i < V; i++) {
        cout << i << "\t\t" << dist[i] << "\n";
    }

    return 0;
}