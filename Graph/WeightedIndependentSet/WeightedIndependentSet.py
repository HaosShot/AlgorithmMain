def mwis(g, w, n, A):
    if n in A:
        return A[n]

    if n == 0:
        return set()

    if n == 1:
        return {1}

    S1 = mwis(g, w, n - 1, A)
    w_S1 = sum(w[v] for v in S1)

    S2 = mwis(g, w, n - 2, A)
    S2 = S2 | {n}
    w_S2 = sum(w[v] for v in S2)

    if w_S1 > w_S2:
        A[n] = S1
    else:
        A[n] = S2
 
    return A[n]

def reconstruct_mwis(w, n, A):
    result = set()
    i = n
    while i >= 1:
        w_S1 = sum(w[v] for v in A[i - 1]) if i - 1 in A else 0
        w_S2 = (sum(w[v] for v in A[i - 2]) + w[i]) if i - 2 in A else w[i]

        if w_S1 < w_S2:
            result.add(i)  
            i -= 2  
        else:
            i -= 1  
    return result

import random

n = 20  
W = {i: random.randint(10000, 100000000) for i in range(1, n + 1)}  

graph = {i: i + 1 for i in range(1, n)}  

A = {}

result = mwis(graph, W, n, A)
reconstructed = reconstruct_mwis(W, n, A)

print("Веса вершин графа:", W)
print("\nМаксимальное независимое множество:", reconstructed)
print("Суммарный вес:", sum(W[v] for v in reconstructed))
