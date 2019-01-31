from node import Node
from edge import Edge
from digraph import Digraph
import dfs
import bfs

nodes = []
for name in range(6):
    nodes.append(Node(str(name)))
g = Digraph()
for n in nodes:
    g.add_node(n)
g.add_edge(Edge(nodes[0], nodes[1]))
g.add_edge(Edge(nodes[1], nodes[2]))
g.add_edge(Edge(nodes[2], nodes[3]))
g.add_edge(Edge(nodes[2], nodes[4]))
g.add_edge(Edge(nodes[3], nodes[4]))
g.add_edge(Edge(nodes[3], nodes[5]))
g.add_edge(Edge(nodes[0], nodes[2]))
g.add_edge(Edge(nodes[1], nodes[0]))
g.add_edge(Edge(nodes[3], nodes[1]))
g.add_edge(Edge(nodes[4], nodes[0]))
sp = dfs.shortest_path(g, nodes[0], nodes[5], to_print=True)
print('Shortest path found by DFS:', dfs.print_path(sp))
sp = bfs.bfs(g, nodes[0], nodes[5], to_print=True)
print('Shortest path found by BFS:', bfs.print_path(sp))