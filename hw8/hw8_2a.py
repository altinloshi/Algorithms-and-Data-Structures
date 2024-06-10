import random
import math

def counting_sort(t_arr):
    sorted_t_arr = [None] * len(t_arr)
    digit_counter = [0] * 10

    for pair in t_arr:
        digit_counter[pair[0]] += 1

    for i in range(1, 10):
        digit_counter[i] += digit_counter[i-1]

    for i in range(len(t_arr)-1, -1, -1):
        sorted_t_arr[digit_counter[t_arr[i][0]]-1] = t_arr[i]
        digit_counter[t_arr[i][0]] -= 1

    return sorted_t_arr

def get_digit(num, n):
    reduced = num // 10**(n-1)
    return reduced % 10

def radix_sort(arr):
    digits = max(len(str(num)) for num in arr)
    for d in range(1, digits+1):
        digit_number = [(get_digit(num, d), num) for num in arr]
        arr = [pair[1] for pair in counting_sort(digit_number)]
    return arr

def generate(size):
    return [random.randint(0, 999) for _ in range(size)]

def main():
    random.seed()
    test_cases = 10
    size = 10

    for _ in range(test_cases):
        arr = generate(size)

        print("Unsorted:", arr)

        largest = max(arr)
        digits = math.ceil(math.log10(largest + 1))
        arr = radix_sort(arr)

        print("Sorted:", arr)

if __name__ == "__main__":
    main()
