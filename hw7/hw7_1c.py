import random

def hoare(arr, low, high): 
  
    pivot = arr[low] 
    i = low - 1
    j = high + 1
  
    while (True): 
  
        i += 1
        while (arr[i] < pivot): 
            i += 1
  
        j -= 1
        while (arr[j] > pivot): 
            j -= 1
  
        if (i >= j): 
            return j 
  
        arr[i], arr[j] = arr[j], arr[i] 

def median_of_three_partition(arr, low, high):
    mid = (low + high) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high]
    if a < b:
        if b < c:
            pivot_index = mid
        elif a < c:
            pivot_index = high
        else:
            pivot_index = low
    else:
        if a < c:
            pivot_index = low
        elif b < c:
            pivot_index = high
        else:
            pivot_index = mid
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return hoare(arr, low, high)

def quicksort_median_of_three(arr, low, high):
    if low < high:
        pivot = median_of_three_partition(arr, low, high)
        quicksort_median_of_three(arr, low, pivot)
        quicksort_median_of_three(arr, pivot + 1, high)

arr = [3, 6, 5, 10, 1, 18, 19, 20]
quicksort_median_of_three(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
