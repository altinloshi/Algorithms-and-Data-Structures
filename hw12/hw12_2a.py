def maximum(num1, num2):
    if num1 >= num2:
        return num1
    return num2

def lst(arr, lines):
    memo = [[0] * lines for _ in range(lines)]

    for i in range(lines):
        for j in range(i + 1):
            memo[i][j] = arr[i][j]

    for i in range(lines - 1, 0, -1):
        for j in range(i, 0, -1):
            memo[i - 1][j - 1] += maximum(memo[i][j], memo[i][j - 1])

    solution = [0] * lines
    i, j = 0, 0
    solution[i] = arr[i][j]

    while i < lines:
        if memo[i][j] > memo[i][j + 1]:
            solution[i] = arr[i][j]
        else:
            solution[i] = arr[i][j + 1]
            j += 1
        i += 1

    print("Maximum sum:", memo[0][0])
    print("Path:", *solution)

def main():
    lines = int(input("Enter the number of lines in the triangle: "))

    arr = []
    print("Enter the triangle elements:")
    for i in range(lines):
        row = list(map(int, input().split()))
        arr.append(row)

    lst(arr, lines)

if __name__ == "__main__":
    main()
