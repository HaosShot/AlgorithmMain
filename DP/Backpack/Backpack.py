def backpack(v, s, C):
    n = len(v)  

    A = []
    for i in range(n + 1):
        row = [0] * (C + 1)
        A.append(row)

    for i in range(1, n + 1):          
        for c in range(C + 1):   
            if s[i - 1] > c:        
                A[i][c] = A[i - 1][c]
            else:                      
                A[i][c] = max(A[i - 1][c], A[i - 1][c - s[i - 1]] + v[i - 1])

    return A, A[n][C]  


def reconstruct_backpack(values, sizes, capacity, A):
    n = len(values)  
    S = []  
    c = capacity  
    
    for i in range(n, 0, -1): 
        if sizes[i - 1] <= c and A[i][c] != A[i - 1][c]:
            S.append(i) 
            c -= sizes[i - 1]  
    
    return S[::-1]  

val = [6000, 1000000, 1200000]  
size = [10000, 2000, 300]     
cap = 50000          

A, max = backpack(val, size, cap)

items = reconstruct_backpack(val, size, cap, A)

print(f"Максимальное суммарное значение: {max}")
print("Выбранные предметы:")
for i in items:
    print(f"Предмет {i}: значение = {val[i - 1]}, размер = {size[i - 1]}")
