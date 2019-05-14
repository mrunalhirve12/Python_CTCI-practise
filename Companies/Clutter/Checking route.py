
import sys

class Graph:
    def minDistance(self, dist, queue):

        minimum = sys.maxsize
        min_index = -1

        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index


    def printPath(self, parent, j):

        # Base Case : If j is source
        if parent[j] == -1:
            print(j)
            return
        self.printPath(parent, parent[j])
        print(j)


    def printSolution(self, dist, parent):
        src = 0
        print("Vertex \t\tDistance from Source\tPath")
        for i in range(1, len(dist)):
            print("\n%d --> %d \t\t%d \t\t\t\t\t" % (src, i, dist[i])),
            self.printPath(parent, i)


    def dijkstra(self, graph, src):

        row = len(graph)
        col = len(graph[0])
        dist = [sys.maxsize] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)

        while queue:
            u = self.minDistance(dist, queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue: #helps not to consider undirected one
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u

        self.printSolution(dist, parent)

def classifyEdges(g_nodes, g_from, g_to, g_weight):
    # Write your code here

    mat = [[0 for x in range(g_nodes+1)]for y in range(g_nodes+1)]
    for i in range(len(g_from)):
        mat[g_from[i]][g_to[i]] = g_weight[i]

    s = Graph()
    s.dijkstra(mat, 1)
    return
