import math 

def insertion_sort(array, left, right):
    for i in range(left + 1, right):
        key = array[i]

        j = i - 1
        while((i >= 0) & (array[j] > key)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def merge_sort(array, left, right, k):
    partition_size = right - left
    if ((partition_size > k)):
        middle = math.floor((left + right) / 2)
        merge_sort(array, left, middle, k)
        merge_sort(array, middle, right, k)
    else:
        insertion_sort(array, left, right)
    


    
array = [1, 7, 6, 2, 5 ,1, 9]
merge_sort(array, 0, len(array), 20)
print(array)