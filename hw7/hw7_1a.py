def lomoto(arr, low, high): 
    pivot = arr[high]  
      
    i = (low - 1) 
    for j in range(low, high): 

        if (arr[j] <= pivot): 
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return (i + 1) 

def quickSort(arr, low, high): 
    if (low < high): 
          

        pi = lomoto(arr, low, high) 
          
        quickSort(arr, low, pi - 1) 
        quickSort(arr, pi + 1, high) 
          
def printArray(arr, size): 
      
    for i in range(size): 
        print(arr[i], end = " ") 
    print() 

arr = [3, 6, 5, 10, 1, 18, 19, 20]
quickSort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)