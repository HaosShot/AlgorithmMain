def karascall(n, e):
    T = []  
    e.sort()  

    def is_acyclic(tree, u, v):
        visited = set()

        def dfs(vertex):
            visited.add(vertex)
            for neighbor in tree.get(vertex, []):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(u)
        return v not in visited

    t = {} 
    for weight, u, v in E:
        if u not in t:
            t[u] = []
        if v not in t:
            t[v] = []

        if is_acyclic(t, u, v):
            T.append((u, v, weight))  
            t[u].append(v)
            t[v].append(u)

        if len(T) == n - 1:  
            break

    return T

n = 5  
E = [
    (1, 0, 1),  
    (3, 0, 2),
    (2, 1, 2),
    (4, 1, 3),
    (5, 2, 3),
    (6, 3, 4)
]

mst = karascall(n, E)
print("Минимальное остовное дерево:")
for u, v, weight in mst:
    print(f"Ребро ({u}, {v}) с весом {weight}")
