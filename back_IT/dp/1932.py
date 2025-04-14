if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                matrix[i][0] += matrix[i - 1][0]
            elif j == i:
                matrix[i][j] += matrix[i - 1][j - 1]
            else:
                matrix[i][j] += max(matrix[i - 1][j], matrix[i - 1][j - 1])

    print(max(matrix[-1]))