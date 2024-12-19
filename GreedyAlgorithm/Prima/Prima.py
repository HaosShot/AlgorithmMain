import time

def prima(graph, start):
    X = {start}  
    T = []       

    while len(X) < len(graph):  
        min_edge = None
        min_cost = float('inf')

        for v in X:
            for w, cost in graph[v]:
                if w not in X and cost < min_cost: 
                    min_edge = (v, w)
                    min_cost = cost

        if min_edge:
            v, w = min_edge
            T.append((v, w, min_cost))  
            X.add(w) 

    return T
graph = {
    'A': [('B', 10000), ('C', 20000), ('D', 50000)],
    'B': [('A', 10000), ('C', 15000), ('E', 25000)],
    'C': [('A', 20000), ('B', 15000), ('F', 30000), ('D', 10000)],
    'D': [('A', 50000), ('C', 10000), ('F', 20000), ('G', 30000)],
    'E': [('B', 25000), ('F', 40000), ('H', 50000)],
    'F': [('C', 30000), ('D', 20000), ('E', 40000), ('H', 60000), ('G', 10000)],
    'G': [('D', 30000), ('F', 10000), ('H', 20000), ('I', 40000)],
    'H': [('E', 50000), ('F', 60000), ('G', 20000), ('I', 30000)],
    'I': [('G', 40000), ('H', 30000), ('J', 70000)],
    'J': [('I', 70000)]
}

s = 'A'
mst = prima(graph, s)
    
print("Минимальное остовное дерево:")
for edge in mst:
    print(f"Ребро: {edge[0]} - {edge[1]}, стоимость: {edge[2]}")

start = time.time()
result = prima(graph, 'A')
end = time.time()

print(f'Время: {end - start:3f}')# медленее 