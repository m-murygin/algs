#!/usr/bin/env python3

# https://www.hackerrank.com/challenges/torque-and-development/problem
from collections import deque


class Graph:
    def __init__(self, size):
        self.size = size
        self.nodes = [[] for _ in range(size)]

    def add_edge(self, i, j):
        if j not in self.nodes[i]:
            self.nodes[i].append(j)
            self.nodes[j].append(i)


def get_network(graph, initial_index, processed):
    network = [initial_index]
    queue = deque([initial_index])
    processed.add(initial_index)

    while len(queue) > 0:
        node_index = queue.popleft()

        for neighbour in graph.nodes[node_index]:
            if neighbour not in processed:
                processed.add(neighbour)
                queue.append(neighbour)
                network.append(neighbour)

    return network


def get_networks(graph):
    processed = set()
    networks = []

    for i in range(graph.size):
        if i not in processed:
            networks.append(get_network(graph, i, processed))

    return networks


def calculate_cost(cities, clib, croad, roads):
    graph = Graph(cities)

    for road in roads:
        graph.add_edge(road[0], road[1])

    networks = get_networks(graph)

    cost = 0
    for network in networks:
        print([x + 1 for x in network])
        # print(f"with_roads: {}")
        # print(f"no_roads: {}")
        cost += min(clib + (len(network) - 1) * croad, clib * len(network))

    return cost


def main():
    cities_count, roads_count, clib, croad = map(int, input().split())

    roads = [None] * roads_count
    for i in range(roads_count):
        l, r = map(int, input().split())
        roads[i] = [l-1, r-1]

    cost = calculate_cost(cities_count, clib, croad, roads)
    print(cost)


if __name__ == "__main__":
    main()
