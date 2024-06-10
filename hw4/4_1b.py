import math 
import random
import time
import matplotlib.pyplot as plt

ARRAY_SIZE = 5

def insertion_sort(array, left, right):
    for i in range(left+1, right):
        key = array[i]

        j = i - 1
        while((j >= left) and (array[j] > key)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def merge(array, left, middle, right):
    left_array = []
    right_array = []
    for i in range(left, middle):
        left_array.append(array[i])

    for i in range(middle, right):
        right_array.append(array[i])

    left_array.append(float('inf'))
    right_array.append(float('inf'))

    i = 0
    j = 0
    for k in range(left, right):
        if (left_array[i] <= right_array[j]):
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1


def insertmerge_sort(array, left, right, k):
    partition_size = right - left
    if (partition_size > k):
        middle = math.floor((left + right) / 2)
        insertmerge_sort(array, left, middle, k)
        insertmerge_sort(array, middle, right, k)  
        merge(array, left, middle, right) 
    else:
        insertion_sort(array, left, right)

def best_case(size):
    return list(range(1, size+1))

def worst_case(size):
    return list(range(size, 0, -1))

def average_case(size):
    return (random.sample(range(1, 100), size))

def current_milli_time():
    return round(time.time() * 1000)


best_case_times = []
average_case_times = []
worst_case_times = []

for i in range(1, ARRAY_SIZE + 1):
    average_case_array = average_case(ARRAY_SIZE)
    start_time = current_milli_time()
    insertmerge_sort(average_case_array, 0, ARRAY_SIZE, i)
    time_taken = current_milli_time() - start_time
    average_case_times.append(time_taken)

    worst_case_array = worst_case(ARRAY_SIZE)
    start_time = current_milli_time()
    insertmerge_sort(worst_case_array, 0, ARRAY_SIZE, i)
    time_taken = current_milli_time() - start_time
    worst_case_times.append(time_taken)

    best_case_array = best_case(ARRAY_SIZE)
    start_time = current_milli_time()
    insertmerge_sort(best_case_array, 0, ARRAY_SIZE, i)
    time_taken = current_milli_time() - start_time
    best_case_times.append(time_taken)

matplotlib.use('TkAgg')

x = range(1, ARRAY_SIZE + 1)
plt.plot(x, best_case_times)
plt.plot(x, average_case_times)
plt.plot(x, worst_case_times)

plt.show()