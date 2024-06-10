import random
import time
import matplotlib.pyplot as plt

# Selection Sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Random sequence generator
def generate_random_sequence(n):
    return [random.randint(1, 1000) for _ in range(n)]

# Case A: Maximum swaps (not decreasingly ordered)
def case_A_sequence(n):
    arr = list(range(1, n))  # Generates an increasing sequence
    return [n] + arr

# Case B: Minimum swaps (already sorted)
def case_B_sequence(n):
    return list(range(1, n+1))

# Function to measure computation time
def measure_time(sequence_generator, n, repetitions=10):
    total_time = 0
    for _ in range(repetitions):
        arr = sequence_generator(n)
        start_time = time.time()
        selection_sort(arr)
        end_time = time.time()
        total_time += end_time - start_time
    return total_time / repetitions

# Testing and plotting
n_values = list(range(1, 101))  # Increase n from 1 to 100
case_A_times = [measure_time(case_A_sequence, n) for n in n_values]
case_B_times = [measure_time(case_B_sequence, n) for n in n_values]
random_times = [measure_time(generate_random_sequence, n) for n in n_values]

# Plotting
plt.plot(n_values, case_A_times, label='Case A')
plt.plot(n_values, case_B_times, label='Case B')
plt.plot(n_values, random_times, label='Random')
plt.xlabel('Input Length (n)')
plt.ylabel('Computation Time (s)')
plt.title('Selection Sort Computation Time')
plt.legend()
plt.grid(True)
plt.show()


