class Graph:
    def __init__(self):
        self.nodes = []

    def add_edge(self, i, j, weight):
        if i not in self.nodes:
            self.nodes[i] = []

        if j not in self.nodes:
            self.nodes[j] = []

        j_weighted = (j, weight)
        if j_weighted not in self.nodes[i]:
            self.nodes[i].append(j_weighted)

        i_weighted = (i, weight)
        if i_weighted not in self.nodes[j]:
            self.nodes[j].append(i_weighted)

    def print(self):
        for index in sorted(self.nodes.keys()):
            print(self.nodes[index])

    def dijkstra(self, start):
        pass

