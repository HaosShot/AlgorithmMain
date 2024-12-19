import heapq
import time 

def prima_heap(graph, start):
    V = set()              
    T = []                     
    min_heap = []                

    for neighbor, cost in graph[start]:
        heapq.heappush(min_heap, (cost, start, neighbor))

    V.add(start)  

    while min_heap and len(V) < len(graph):
        cost, v, w = heapq.heappop(min_heap)  

        if w not in V:  
            V.add(w)    
            T.append((v, w, cost))  

            for neighbor, e in graph[w]:
                if neighbor not in V:
                    heapq.heappush(min_heap, (e, w, neighbor))

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
t = prima_heap(graph, s)

print("Минимальное остовное дерево:")
for edge in t:
    print(f"Ребро: {edge[0]} - {edge[1]}, стоимость: {edge[2]}")

start = time.time()
result = prima_heap(graph, 'A')
end = time.time()

print(f'Время: {end - start:3f}') # быстрее чем обычный Прима