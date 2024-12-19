import random
import time

def optimal_search_tree(p):
    n = len(p)
    A = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        A[i][i - 1] = 0

    sum_p = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_p[i] = sum(p[:i])

    for s in range(1, n + 1):
        for i in range(1, n - s + 1):
            j = i + s - 1
            A[i][j] = sum_p[j] - sum_p[i - 1] + min(A[i][r - 1] + A[r + 1][j] for r in range(i, j + 1))

    return A[1][n]

n = 100
p = [random.uniform(0, 1) for _ in range(n)]

start = time.time()
result = optimal_search_tree(p)
end = time.time()

print(f"Минимальное взвешенное время поиска для {n} ключей: {result}")
print(f"Время выполнения: {end - start} ")
