#!/usr/bin/env python3

import DisjointSet

class UndirectedWeightedGraph:
    def __init__(self, vertices=[], edges={}):
        self.vertices = vertices

        # edge format: { (vertex_1, vertex_2): weight }
        # vertices are sorted in tuple
        self.edges = edges
        return

    def add_vertex(self, vertex):
        if not vertex in self.vertices:
            self.vertices.append(vertex)
            return True
        else:
            return False

    def add_edge(self, vertex_1, vertex_2, weight=1):
        vertices = tuple([vertex_1, vertex_2].sort())
        self.edges[vertices] = weight

    def get_mst_kruskal(self):
        disjoint_set = DisjointSet.DisjointSet(self.vertices)

        # sort edges by weight
        sorted_edges = sorted(graph.edges,
                              key = lambda edge: self.edges[edge])

        mst_edges = []
        
        for edge in sorted_edges:
            if disjoint_set.unify(edge[0], edge[1]):
                mst_edges.append(edge)

        return mst_edges

vertices = ['a', 'b', 'c', 'd', 'e']
edge_list = {
    ('a', 'e'): 1,
    ('a', 'b'): 3,
    ('b', 'e'): 4,
    ('c', 'e'): 6,
    ('b', 'c'): 5,
    ('d', 'e'): 7,
    ('c', 'd'): 2
}

graph = UndirectedWeightedGraph(vertices, edge_list)

print(graph.get_mst_kruskal())
