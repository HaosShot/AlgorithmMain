import time
def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            recursive_dfs(graph, neighbor, visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = time.time()
result = recursive_dfs(graph, 'A')
end = time.time()

result = recursive_dfs(graph, 'A')
print("Достижимые вершины:", list(result))

print("Время: ", end - start) 