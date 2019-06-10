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


    def printSolution(self, dist, parent, dest):
        for i in range(1, len(dist)):
            if i==dest:
                return dist[i]


    def dijkstra(self, graph, src, dest):

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

        minval=self.printSolution(dist, parent,dest)
        return minval


def IsTrusted(node,trustedGraph,pretrustedPeers,trustThreshold):
    if node in pretrustedPeers:
        return True
    g=Graph()
    minvalue=g.dijkstra(trustedGraph, node, pretrustedPeers[0])
    if minvalue <= trustThreshold:
        return True
    else:
        return False