def MergeSort(arr):
    if len(arr) <= 1: 
        return arr
    
    mid_point = len(arr) // 2
    left_arr = MergeSort(arr[0:mid_point:])  
    right_arr = MergeSort(arr[mid_point::])  

    return Merge(left_arr, right_arr)

def Merge(left_arr, right_arr):
    result = []
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result.extend(left_arr[i::])
    result.extend(right_arr[j::])
    return result

arr = [123123, 5135312521, 56789, 98765, 152391582, 5555555]

sorted_arr = MergeSort(arr)
print(f'Отсортированный массив: {sorted_arr}')
