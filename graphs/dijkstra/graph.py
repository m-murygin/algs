class Graph:
    def __init__(self, size):
        self.nodes = [[] for _ in range(size)]

    def add_edge(self, i, j, weight):
        j_weighted = (j, weight)
        if j_weighted not in self.nodes[i]:
            self.nodes[i].append(j_weighted)

        i_weighted = (i, weight)
        if i_weighted not in self.nodes[j]:
            self.nodes[j].append(i_weighted)

    def print(self):
        for node in self.nodes:
            print(node)

    # def dijkstra(self, start):
    #     shortes_paths = {}
    #     # (cur, parent, weight)
    #     crossing_edges = {}
    #     crossing_edges[start] = 0

    #     while len(crossing_edges) > 0:
    #         min_edge = min(crossing_edges, key=lambda t:t[1])
    #         crossing_edges.remove(min_edge)
    #         shortes_paths[min_edge] = min_edge[1]

    #         for edge in self.nodes[min_edge]:
