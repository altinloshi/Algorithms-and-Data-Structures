import time
import math

N = 20

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
def fibonacci_bottom_up(n):
    fibFirst = 0
    fibSecond = 1
    for i in range (2, n+1):
        fibNext = fibFirst + fibSecond
        fibFirst = fibSecond
        fibSecond = fibNext
    return fibSecond


def fibonacci_closed_form(n):
    return (pow(((1+math.sqrt(5))/2), n)/math.sqrt(5))

def fibonacci_matrix(n):
    matrix = [1, 1, 1, 0]
    matrixNext = []
    matrixNext.append(matrix[0]*matrix[0]+matrix[1]*matrix[2])
    matrixNext.append(matrix[0]*matrix[1]+matrix[1]*matrix[3])
    matrixNext.append(matrix[3]*matrix[2]+matrix[3]*matrix[2])
    matrixNext.append(matrix[3]*matrix[1]+matrix[3]*matrix[3])
    for i in range (n):
        matrix = matrixNext

    return matrix[1]

def measure_time(method, n):
    start_time = time.time()
    method(n)
    return time.time() - start_time

max_time = 1.0

results_recursive = []
results_bottom_up = []
results_closed_form = []
results_matrix = []

for i in range(N):
    recursive_time = measure_time(fibonacci_recursive, i)
    bottom_up_time = measure_time(fibonacci_bottom_up, i)
    closed_form_time = measure_time(fibonacci_closed_form, i)
    matrix_time = measure_time(fibonacci_matrix, i)
    results_recursive.append(recursive_time)
    results_bottom_up.append(bottom_up_time)
    results_closed_form.append(closed_form_time)
    results_matrix.append(matrix_time)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(list(range(N)), results_recursive, label="Recursive")
plt.plot(list(range(N)), results_bottom_up, label="Bottom Up")
plt.plot(list(range(N)), results_closed_form, label="Closed Form")
plt.plot(list(range(N)), results_matrix, label="Matrix")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.title("Running Times of Fibonacci Methods")
plt.legend()
plt.grid(True)
plt.show()
