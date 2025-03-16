import sys

def dfs(col, answer):
    if col == n - 1:
        return min(fuel, answer)
    for i in dir:


if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dir = [1, -1, 0]

    fuel = sys.maxsize

    for i in range(m):
        fuel = min(dfs(0, matrix[0][i]))


