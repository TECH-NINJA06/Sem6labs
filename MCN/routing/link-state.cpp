#include <iostream>
#include <climits>

using namespace std;

int main() {
    int n, src;
    cout << "Enter number of nodes: ";
    cin >> n;
    int INF = INT_MAX; 
    
    int cost[n][n], dist[n], visited[n];

    cout << "Enter cost matrix (use 9999 for no direct link):\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> cost[i][j];
        }
        visited[i] = 0;
    }

    cout << "Enter source node (0 to " << n-1 << "): ";
    cin >> src;

    for (int i = 0; i < n; i++) {
        dist[i] = cost[src][i];
    }
    dist[src] = 0;
    visited[src] = 1;

    for (int count = 0; count < n - 1; count++) {
        int min = INF, u = -1;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i] && dist[i] < min) {
                min = dist[i];
                u = i;
            }
        }
        
        if (u == -1) break; 
        visited[u] = 1;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && cost[u][v] != INF && dist[u] + cost[u][v] < dist[v]) {
                dist[v] = dist[u] + cost[u][v];
            }
        }
    }

    cout << "\nRouting Table for Node " << src << ":\n";
    cout << "Destination\tShortest Distance\n";
    for (int i = 0; i < n; i++) {
        cout << i << "\t\t" << dist[i] << "\n";
    }

    return 0;
}