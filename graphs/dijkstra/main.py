#!/usr/bin/python3

import sys
from graph import Graph


def read_graph(filepath):
    with open(filepath) as fp:
        graph = Graph(200)

        for line in fp:
            node = line.split()
            tail = int(node[0])
            for i in range(1, len(node)):
                head, weight = map(int, node[i].split(','))
                graph.add_edge(tail-1, head-1, weight)

    return graph


def main():
    filepath = sys.argv[1]
    graph = read_graph(filepath)

    graph.dijkstra(0)

    result = []
    for i in map(int, "7,37,59,82,99,115,133,165,188,197".split(",")):
        result.append(str(graph.nodes[i-1].min_path))

    print(",".join(result))


if __name__ == "__main__":
    main()
