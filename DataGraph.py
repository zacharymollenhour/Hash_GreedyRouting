# Zachary Mollenhour #001462017
"""
Function Responsible for determining the minimumDistance between all connected vertices
It will check if a location has been visited already and if not, determine the minimum distances
"""
def minumumDistance(vertex, distance, visited):
    minimum = float('inf')

    #We will loop through all of the not vertex and look for nonvisted ones
    for v in range(vertex):
        if distance[v] < minimum and visited[v] == False:
            minimum = distance[v]
            minimum_index = v

    return minimum_index

"""
Class that represents a Graph of packages and their minimum distances
"""
class DataGraph:

    #Initialize a object of DataGraph Class
    #Paramater of the graph Vertices 
    def __init__(self, graphVertices):
        self.vertices = graphVertices
        self.graph = [[0 for column in range(graphVertices)] for row in range(graphVertices)]

    #Function that adds an edge to the DataGraph Object
    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    #Function to remove an edge from the DataGraph object
    def remove_edge(self, v1, v2):
        if self.graph[v1][v2] == 0:
            return
        self.graph[v1][v2] = -1
        self.graph[v2][v1] = -1

    #Function to get the calculated distance between two graph locations (package addresses)
    def get_distance(self, v1, v2):
        return self.graph[v1][v2]

    # Function to find the shortest path possible between the package destinations
    def shortestPathAlogirthim(self, src):
        dist = [float('inf')] * self.vertices

        dist[src] = 0
        visited = [False] * self.vertices

        for cout in range(self.vertices):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = minumumDistance(self.vertices, dist, visited)

            # Put the minimum distance vertex in the
            # shotest path tree
            visited[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and visited[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = round(dist[u] + self.graph[u][v], 1)

        return dist

    # Because the is complete graph we can run
    # a optimization algothrim that loops through
    # every node can caculates the shortest path
    # for to every other node
    def optimize(self):
        optimal_distances = []
        for i in range(0, len(self.graph)):
            dist = self.dijkstra(i)
            optimal_distances.append(dist)
        return optimal_distances

