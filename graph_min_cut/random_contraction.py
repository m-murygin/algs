#!/usr/bin/python

import argparse
from random import randint

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
        self.edges = list()

    def __str__(self):
        edges_str = ', '.join([str(e) for e in self.edges])
        return '(%s) [%s]' % (self.id, edges_str)

class Edge(object):
    def __init__(self, head, tail):
        super(Edge, self).__init__()
        self.head = head
        self.tail = tail

    def __str__(self):
        return '%s:%s' % (self.head.id, self.tail.id)


def find_min_cut(vertices, edges):
    """Fins min cut

    Args:
        vertices (dict): list of graph vertices
        edges (dict): list of graph edges

    Returns:
        number: min cut edges count
    """
    remains_iterations = len(vertices) - 2
    while remains_iterations > 0:
        contracted_edge_index = randint(0, len(edges)-1)
        contracted_edge = edges[contracted_edge_index]

        base_vertex = contracted_edge.head
        contracted_vertex = contracted_edge.tail

        for edge in contracted_vertex.edges:
            # remove self-referenced edges
            if edge.head.id == base_vertex.id or edge.tail.id == base_vertex.id:
                base_vertex.edges.remove(edge)
                edges.remove(edge)
            elif edge.head.id == contracted_vertex.id:
                edge.head = base_vertex
            else:
                edge.tail = base_vertex

        vertices.remove(contracted_vertex)
        edges.remove(contracted_edge)

        remains_iterations -= 1

    return len(vertices[0].edges)


def parse_input_file(filename):
    vertices = list()
    edges = list()

    with open(filename) as f:
        lines = f.readlines()

        # fill vertices
        for line in lines:
            vertex_id = int(line.split(' ')[0])
            vertices.append(Vertex(vertex_id))

        # fill edges
        for line in lines:
            line_ints = [int(x) for x in line.split(' ')]
            # get edge vertex
            head_vertex = vertices[line_ints.pop(0) - 1]

            for tail_id in line_ints:
                tail_vertex = vertices[tail_id - 1]
                edge = Edge(head_vertex, tail_vertex)
                edges.append(edge)
                head_vertex.edges.append(edge)

    return (vertices, edges)

def main():
    parse_result = parse_input_file(args.filename)
    vertices = parse_result[0]
    edges = parse_result[1]

    # for v in vertices:
    #     print v
    # for e in edges:
    #     print e

    print find_min_cut(vertices, edges)

if __name__ == '__main__':
    main()

