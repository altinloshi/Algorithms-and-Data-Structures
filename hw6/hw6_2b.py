def heapify(arr, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and arr[i] < arr[l]:
          largest = l
  
      if r < n and arr[largest] < arr[r]:
          largest = r
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  
  
def heapSort(arr):
    n = len(arr)
  

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
  
    for i in range(n-1, 0, -1):

        arr[i], arr[0] = arr[0], arr[i]
  
        heapify(arr, i, 0)
        j = 0
        while True:
            largest = j
            left = 2 * j + 1
            right = 2 * j + 2

            if left < j and arr[left] > arr[largest]:
                largest = left

            if right < j and arr[right] > arr[largest]:
                largest = right

            if largest != j:
                arr[j], arr[largest] = arr[largest], arr[j]
                j = largest
            else:
                break
  
  
arr = [1, 12, 9, 5, 6, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
print(arr)