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
  
  
def quickSort(arr, low, high): 

    if (low < high): 
  
        pi = hoare(arr, low, high) 
  
        quickSort(arr, low, pi) 
        quickSort(arr, pi + 1, high) 
  
  
def printArray(arr, n): 
    for i in range(n): 
        print(arr[i], end=" ") 
    print() 

arr = [3, 6, 5, 10, 1, 18, 19, 20]
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
