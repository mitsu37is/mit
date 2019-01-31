class Digraph(object):
    """nodes は Node オブジェクトのリストである
       edges は各 node をその node の子ノードのリストにマップする辞書である"""
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []

    def add_edge(self, edge):
        src = edge.get_src()
        dest = edge.get_destination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def children_of(self, node):
        return self.edges[node]

    def has_node(self, node):
        return node in self.nodes

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.get_name() + ' -> ' + dest.get_name + '\n'
        return result[-1]