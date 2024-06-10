def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        bi = int(n * num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

arr = [0.9, 0.1, 0.6, 0.7, 0.6, 0.3, 0.1]
bucket_sort(arr)
print("Sorted array is")
print(" ".join(map(str, arr)))