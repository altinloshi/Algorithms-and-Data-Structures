def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 256
    
    for i in range(n):
        index = ord(arr[i][exp]) if len(arr[i]) > exp else 0
        count[index] += 1

    for i in range(1, 256):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = ord(arr[i][exp]) if len(arr[i]) > exp else 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_length = max(len(word) for word in arr)
    for exp in range(max_length - 1, -1, -1):
        counting_sort(arr, exp)

words = ["word", "category", "cat", "new", "news", "world", "bear", "at", "work", "time"]
radix_sort(words)
print(words)
