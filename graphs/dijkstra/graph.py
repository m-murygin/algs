import math


class Edge:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

    def __eq__(self, other):
        return self.to == other.to and self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return f"({self.to}, {self.weight})"


class Node:
    def __init__(self):
        self.edges = []
        self.min_path = math.inf
        self.has_final_path = False

    def __lt__(self, other):
        return self.min_path < other.min_path

    def __str__(self):
        return f"{self.min_path}: [{' '.join(map(str, self.edges))}]"


class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [Node() for _ in range(size)]

    def add_edge(self, i, j, weight):
        j_edge = Edge(j, weight)
        if j_edge not in self.nodes[i].edges:
            self.nodes[i].edges.append(j_edge)

        i_edge = Edge(i, weight)
        if i_edge not in self.nodes[j].edges:
            self.nodes[j].edges.append(i_edge)

    def print(self):
        for node in self.nodes:
            print(node)

    def dijkstra(self, start):
        self.nodes[start].min_path = 0

        unprocessed_nodes = []
        for edge in self.nodes[start].edges:
            to_node = self.nodes[edge.to]
            to_node.min_path = edge.weight
            to_node.has_final_path = True
            unprocessed_nodes.append(to_node)

        while len(unprocessed_nodes) > 0:
            node = min(unprocessed_nodes)
            node.has_final_path = True

            for edge in node.edges:
                to_node = self.nodes[edge.to]
                # we already calculated minpath for this node
                if to_node.has_final_path:
                    continue

                new_min_path = node.min_path + edge.weight

                # we met this node for the first time
                if to_node.min_path == math.inf:
                    to_node.min_path = new_min_path
                    unprocessed_nodes.append(to_node)

                # we have this node in unprocessed list
                to_node.min_path = min(to_node.min_path, new_min_path)

            unprocessed_nodes.remove(node)
