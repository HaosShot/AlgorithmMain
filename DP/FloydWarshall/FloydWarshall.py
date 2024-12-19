import math

def floyd_warshall(n, graph):
    A = [[[float('inf')] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]

    for v in range(1, n + 1):
        for w in range(1, n + 1):
            if v == w:
                A[0][v][w] = 0
            elif graph[v-1][w-1] != 0:  
                A[0][v][w] = graph[v-1][w-1]
            else:
                A[0][v][w] = float('inf')  

    for k in range(1, n + 1):
        for v in range(1, n + 1):
            for w in range(1, n + 1):
                A[k][v][w] = min(A[k-1][v][w], A[k-1][v][k] + A[k-1][k][w])

    for v in range(1, n + 1):
        if A[n][v][v] < 0:
            return "есть отрицательный цикл"

    return A[n][1][w]  

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

result = floyd_warshall(n, graph)
print("Кратчайшее расстояние между 1 и 10:", result)
