import sys

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    sorted_matrix = [sorted(row) for row in matrix]

    left, middle, right = 0, 0, 0
    answer = sys.maxsize

    while True:
        if left == m -1 and middle == m - 1 and right == m - 1:
            print(answer)
            break
