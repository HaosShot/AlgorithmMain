import time
def iterative_dfs(graph, s):
    visited = set()
    stack = [s]
    reachable = []

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            reachable.append(v)
            for neighbor in graph.get(v, []):
                stack.append(neighbor)

    return reachable

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
result = iterative_dfs(graph, 'A')
print("Достижимые вершины:", result)

start = time.time()
result = iterative_dfs(graph, 'A')
end = time.time()

print("Время: ", end - start)