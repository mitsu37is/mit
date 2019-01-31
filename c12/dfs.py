def print_path(path):
    """path は Node オブジェクトからなるリストとする"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '→'
    return result

def dfs(graph, start, end, path, shortest, to_print=False):
    """graph は Digraph オブジェクト, start と end は Node オブジェクト
       path と shortest は Node オブジェクトのリストとする
       graph での start から end への最短経路を返す"""
    path = path + [start]
    if to_print:
        print('Current DFS path: ', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = dfs(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest

def shortest_path(graph, start, end, to_print=False):
    """graph は Digraph オブジェクト, start と end は Node オブジェクトとする
       graph での, start から end への最短経路を返す"""
    return dfs(graph, start, end, [], None, to_print)