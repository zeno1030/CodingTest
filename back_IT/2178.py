from collections import deque

from pygments.lexers import graph


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))

    return matrix[n-1][m-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix = [list(map(int, input())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(bfs(0, 0))
