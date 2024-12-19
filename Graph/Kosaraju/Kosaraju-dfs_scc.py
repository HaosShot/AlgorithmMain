def kosaraju(graph):

    def dfs(graph, v, visited, result):
 
        visited.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(graph, neighbor, visited, result)
        result.append(v)

    visited = set()
    finish_order = []
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited, finish_order)

    transposed_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)

    visited.clear()
    scc_list = []
    while finish_order:
        node = finish_order.pop()
        if node not in visited:
            scc = []
            dfs(transposed_graph, node, visited, scc)
            scc_list.append(scc)

    return scc_list

graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'B': ['D'],
    'D': ['E'],
    'E': ['F'],
    'F': ['D'],
    'G': ['F'],
    'G': ['H'],
    'H': ['I'],
    'I': ['G']
}

scc_result = kosaraju(graph)
print(scc_result)
