#!/usr/bin/python

import argparse
import pprint
from random import randint

pp = pprint.PrettyPrinter(indent=2)

parser = argparse.ArgumentParser(
    description='Search min cut in the input graph')
parser.add_argument('filename', type=str,
                    help='file to read a graph. Format: ' +
                    'vertex1 vertex1_neighbor1 vertex1_neighbor2\\n ' +
                    'vertex2 vertex2_neighbor1 vertex1_neighbor2\\n')
args = parser.parse_args()

class Vertex(object):
    def __init__(self, _id):
        super(Vertex, self).__init__()
        self.id = _id
        self.edges = []

    def __str__(self):
        edges_str = ', '.join([str(e) for e in self.edges])
        return '%s [%s]' % (self.id, edges_str)

class Edge(object):
    def __init__(self, head, tail):
        super(Edge, self).__init__()
        self.head = head
        self.tail = tail

    def __str__(self):
        return '%s:%s' % (self.head, self.tail)


def parse_input_file(filename):
    vertices = []
    edges = []

    with open(filename) as f:
        for line in f:
            line_list = [int(x) for x in line.split(' ')]
            vertex_id = line_list.pop(0)
            vertex = Vertex(vertex_id)

            for edge_tail in line_list:
                edge = Edge(vertex_id, edge_tail)
                edges.append(edge)
                vertex.edges.append(edge)

            vertices.append(vertex)

    return (vertices, edges)

def main():
    parse_result = parse_input_file(args.filename)
    vertices = parse_result[0]
    edges = parse_result[1]

    for v in vertices:
        print v
    for e in edges:
        print e

if __name__ == '__main__':
    main()

