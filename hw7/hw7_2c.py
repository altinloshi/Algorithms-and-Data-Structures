import random
from typing import Tuple

def partition(arr: list, begin: int, end: int) -> Tuple[int, int]:
    size = end - begin

    random_IND = random.randint(begin, end - 1)
    arr[begin], arr[random_IND] = arr[random_IND], arr[begin]

    random_IND = random.randint(begin, end - 1)
    arr[begin + 1], arr[random_IND] = arr[random_IND], arr[begin + 1]

    if arr[begin] > arr[begin + 1]:
        arr[begin], arr[begin + 1] = arr[begin + 1], arr[begin]
    arr[begin + 1], arr[end - 1] = arr[end - 1], arr[begin + 1]

    i = begin
    for k in range(begin + 1, end - 1):
        if arr[k] < arr[begin]:
            i += 1
            arr[k], arr[i] = arr[i], arr[k]
    arr[begin], arr[i] = arr[i], arr[begin]

    j = end - 1
    for k in range(end - 2, i, -1):
        if arr[k] > arr[end - 1]:
            j -= 1
            arr[k], arr[j] = arr[j], arr[k]
    arr[end - 1], arr[j] = arr[j], arr[end - 1]

    return i, j

def quicksort(arr: list, begin: int, end: int) -> None:
    if begin < end - 1:

        pivots = partition(arr, begin, end)

        quicksort(arr, begin, pivots[0])
        quicksort(arr, pivots[0] + 1, pivots[1])
        quicksort(arr, pivots[1] + 1, end)

if __name__ == "__main__":
    random.seed(0)
    test_cases = 10 
    size = 10  

    print("Quicksort with two random pivots:")
    for _ in range(test_cases):
        arr = [random.randint(0, 49) for _ in range(size)]

        print("Unsorted array:", arr)

        quicksort(arr, 0, size)

        print("Sorted array:", arr, "\n")
