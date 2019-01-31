from digraph import Digraph
from edge import Edge

class Graph(Digraph):
    def add_edge(self, edge):
        Digraph.add_edge(self, edge)
        rev = Edge(edge.get_destination(), edge.get_src())
        Digraph.add_edge(self, rev)
