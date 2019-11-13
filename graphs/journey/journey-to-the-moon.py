#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/journey-to-the-moon/problem

import math
from collections import deque


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.nodes = [[] for i in range(size)]

    def add_edge(self, i, j):
        if not (j in self.nodes[i]):
            self.nodes[i].append(j)
            self.nodes[j].append(i)

    def print(self):
        for i in range(self.size):
            print(self.nodes[i])


def find_network_members(graph, index, processed):
    queue = deque([index])
    members = []
    while len(queue) != 0:
        current = queue.popleft()
        print(f"Before: {current}, {members}, {queue}, {processed}")

        if current in processed:
            continue

        members.append(current)
        processed.add(current)
        for node in graph.nodes[current]:
            queue.append(node)

        print(f"After: {current}, {members}, {queue}, {processed}")

    return members


def find_networks(n, edges):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    processed = set()
    networks = []
    for i in range(n):
        if i in processed:
            continue

        members = find_network_members(graph, i, processed)
        if len(members) != 1:
            networks.append(members)

    print(networks)
    return networks


def calc_pairs(n):
    if n == 1:
        return 0

    return math.factorial(n) // (2*math.factorial(n - 2))


def main():
    n, p = map(int, input().split())

    edges = []
    for _ in range(p):
        edges.append(list(map(int, input().rstrip().split())))

    networks = find_networks(n, edges)
    total_pairs = calc_pairs(n)
    for network in networks:
        total_pairs -= calc_pairs(len(network))

    print(total_pairs)


if __name__ == "__main__":
    main()
