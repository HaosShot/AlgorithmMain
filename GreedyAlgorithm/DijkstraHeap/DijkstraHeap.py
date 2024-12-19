import heapq

def dijkstra_heap(graph, s):
    X = {s}  
    H = [] 
    key = {}  

    for v in graph:
        key[v] = float('inf')
    key[s] = 0

    for v in graph:
        heapq.heappush(H, (key[v], v))

    while H: 
        current_key, w_star = heapq.heappop(H)

        X.add(w_star)

        len_w_star = key[w_star]

        for neighbor, weight in graph[w_star]:
            if neighbor not in X:
                new_key = len_w_star + weight
                if new_key < key[neighbor]:
                    key[neighbor] = new_key
                    heapq.heappush(H, (key[neighbor], neighbor))

    return key

graph = {
    's': [('a', 10000000), ('b', 4000000)],
    'a': [('b', 200000000), ('c', 5000000000)],
    'b': [('c', 100000000)],
    'c': []
}

start = 's'
result = dijkstra_heap(graph, start)
print("Минимальные расстояния:", result)

input("Enter для выхода")
