from collections import deque


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, i, j):
        if i not in self.nodes:
            self.nodes[i] = []

        if j not in self.nodes:
            self.nodes[j] = []

        if j not in self.nodes[i]:
            self.nodes[i].append(j)
            self.nodes[j].append(i)

    def print(self):
        for index in sorted(self.nodes.keys()):
            print(self.nodes[index])

    def get_networks(self):
        networks = []

        processed = set()
        for node in self.nodes:
            if node in processed:
                continue

            networks.append(0)
            queue = deque([node])
            while len(queue) > 0:
                el = queue.popleft()
                if el in processed:
                    continue

                processed.add(el)
                networks[-1] += 1
                for edge in self.nodes[el]:
                    queue.append(edge)

        return networks
