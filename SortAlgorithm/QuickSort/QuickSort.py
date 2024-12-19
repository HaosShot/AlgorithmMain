import random
import time

a = []

def pull(arr):
    for _ in range(1000000): 
        arr.append(random.randint(5000, 50000))

pull(a)

def quicksort(arr):
    if len(arr) <= 1:  
        return arr

    pivot = arr[len(arr) // 2]  

    left = []  
    middle = []  
    right = [] 

    for x in arr:  
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return quicksort(left) + middle + quicksort(right)  


start_builtin = time.time()
sorted_builtin = sorted(a)
end_builtin = time.time()

start_quicksort = time.time()
sorted_quick = quicksort(a)
end_quicksort = time.time()

print("Время встроенной сортировки:", end_builtin - start_builtin, "секунд")
print("Время QuickSort:", end_quicksort - start_quicksort, "секунд")
