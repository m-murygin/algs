#!/usr/bin/python3

import sys
from graph import Graph


def read_graph(filepath):
    graph = Graph()
    with open(filepath) as fp:
        for line in fp:
            node = line.split()

            tail = int(node[0])
            for i in range(1, len(node)):
                head, weight = map(int, node[i].split(','))
                graph.add_edge(tail - 1, head - 1, weight)

    return graph


def main():
    filepath = sys.argv[1]
    graph = read_graph(filepath)
    graph.print()


if __name__ == "__main__":
    main()
