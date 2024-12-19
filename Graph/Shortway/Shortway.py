def short_way(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0  
  
    Q = [start]
    
    while Q:
        V = Q.pop(0) 
        
        for neighbors in graph[V]: 
            if dist[neighbors] == float('inf'):  
                dist[neighbors] = dist[V] + 1  
                Q.append(neighbors)  
    
    return dist

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['B', 'J'],
    'G': ['C', 'K'],
    'H': ['D', 'J'],
    'I': ['E', 'K'],
    'J': ['F', 'H'],
    'K': ['G', 'I']
}

s = 'A'
short = short_way(graph, s)

print(f"Кратчайшие расстояния от вершины '{s}':")
for v, dist in short.items():
    print(f"Расстояние до {v}: {dist}")
