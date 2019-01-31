def print_path(path):
    """path は Node オブジェクトからなるリストとする"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '→'
    return result

def bfs(graph, start, end, to_print=False):
    """graph は Digraph オブジェクト, start と end は Node オブジェクトとする
       graph での start ノードから end ノードへの最短経路を返す"""
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(tmp_path))
        last_node = tmp_path[-1]
        if last_node == end:
            return tmp_path
        for next_node in graph.children_of(last_node):
            if next_node not in tmp_path:
                new_path = tmp_path + [next_node]
                path_queue.append(new_path)
    return None
