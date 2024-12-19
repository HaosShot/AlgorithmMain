import math

def bellman_ford(n, graph, start_vertex):
    A = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    A[0][start_vertex] = 0

    for i in range(1, n + 1):
        stop = True
        for v in range(1, n + 1):
            for w in range(1, n + 1):
                if A[i-1][w] + graph[w-1][v-1] < A[i][v]:
                    A[i][v] = A[i-1][w] + graph[w-1][v-1]
                    stop = False
        if stop:
            return A[i-1][v]

    for v in range(1, n + 1):
        if A[n][v] < 0:
            return "есть отрицательный цикл"

    return A[n][v]

n = 10
graph = [
    [0, 3, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    [3, 0, 1, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, 1, 0, 7, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, 7, 0, 2, math.inf, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, 2, 0, 4, math.inf, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 4, 0, 5, math.inf, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, math.inf, 5, 0, 6, math.inf, math.inf],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 6, 0, 3, 2],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 3, 0, 7],
    [math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, math.inf, 2, 7, 0]
]

graph[0][9] = 15  

result = bellman_ford(n, graph, 1) 
print("Кратчайшее расстояние от вершины 1 до 10:", result)
