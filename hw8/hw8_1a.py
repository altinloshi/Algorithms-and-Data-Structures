def count_sort(array):
   
    M = max(array)
 
    count_array = [0] * (M + 1)

    for num in array:
        count_array[num] += 1
 
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    output_array = [0] * len(array)
 
    for i in range(len(array) - 1, -1, -1):
        output_array[count_array[array[i]] - 1] = array[i]
        count_array[array[i]] -= 1
 
    return output_array
 

if __name__ == "__main__":

    input_array = [9, 1, 6, 7, 6, 2, 1]
 
    output_array = count_sort(input_array)
    print("Sorted array is")

    for num in output_array:
        print(num, end=" ")