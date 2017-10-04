#!/usr/bin/env python3

class DisjointSet:
    def __init__(self, vertices=[]):
        # format: { 'item': node_value, 'parent': node_parent}
        self.vertices = {}

        for vertex in vertices:
            self.add_item(vertex)

    def add_item(self, new_item):
        if new_item in self.vertices:
            return False
        else:
            self.vertices[new_item] = new_item
            return True

    def find_root(self, item):
        if self.vertices[item] == item:
            return item
        else:
            return self.find_root(self.vertices[item])

    def unify(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        if x_root == y_root:
            return False # not disjoint
        else:
            self.vertices[x_root] = y_root
            return True # disjoint

    def is_disjoint(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        if x_root == y_root:
            return False
        else:
            return True
