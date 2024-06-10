def lis(arr):
    size = len(arr)
    lis_values = [1] * size

    for i in range(1, size):
        subproblems = []
        for k in range(i):
            if arr[k] < arr[i]:
                subproblems.append(lis_values[k])

        if subproblems:
            lis_values[i] = 1 + max(subproblems)
        else:
            lis_values[i] = 1

    solution_ind = lis_values.index(max(lis_values))
    i = lis_values[solution_ind]
    solution_arr = [0] * i

    solution_arr[i - 1] = arr[solution_ind]

    while solution_ind != 0:
        solution_ind -= 1
        if lis_values[solution_ind] < lis_values[solution_ind + 1]:
            i -= 1
            solution_arr[i - 1] = arr[solution_ind]
        else:
            continue

    for elem in solution_arr:
        print(elem, end=" ")

if __name__ == "__main__":
    size = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

    lis(arr)

