#!/usr/bin/env python3
# https://www.hackerrank.com/challenges/bfsshortreach/problem

from collections import deque


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.nodes = [[] for i in range(size)]

    def add_edge(self, i, j):
        if not (j in self.nodes[i-1]):
            self.nodes[i-1].append(j)
            self.nodes[j-1].append(i)

    def print(self):
        for i in range(self.size):
            print(self.nodes[i])


def bfs(n, m, edges, s):
    graph = Graph(n)
    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    graph.print()

    res = [-1] * (n - 1)

    processed = set([s])
    queue = deque(maxlen=n)
    queue.append((s, 0))
    while len(queue) != 0:
        el, layer = queue.popleft()

        if el < s:
            res[el - 1] = layer * 6
        elif el > s:
            res[el - 2] = layer * 6

        for neighbour in graph.nodes[el - 1]:
            if neighbour not in processed:
                queue.append((neighbour, layer + 1))
                processed.add(neighbour)

        print(el, layer, queue)

    return res


def main():
    n, m = map(int, input().split())

    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    s = int(input())

    result = bfs(n, m, edges, s)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
