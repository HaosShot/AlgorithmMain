def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)
   
    while queue:
        v = queue.pop(0)
        print(f"Посещаем вершину: {v}")

        for w in graph.get(v, []): 
            if w not in visited:   
                visited.add(w)    
                queue.append(w)    

    return visited

graph = {
    's': ['v1', 'v2'],
    'v1': ['v3', 'v4'],
    'v2': ['v4'],
    'v3': [],
    'v4': ['v5'],
    'v5': []
}
s = 's'
reachable_vertices = bfs(graph, s)
print("Достижимые вершины из", s, ":", reachable_vertices)
