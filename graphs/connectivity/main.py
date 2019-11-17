#!/usr/bin/python3

import sys
from graph import Graph


def read_graph(filepath):
    graph = Graph()
    with open(filepath) as fp:
        for line in fp:
            i, j = map(int, line.split())
            graph.add_edge(i, j)

    return graph


def main():
    filepath = sys.argv[1]
    graph = read_graph(filepath)
    networks = graph.get_networks()
    print(networks)


if __name__ == "__main__":
    main()
