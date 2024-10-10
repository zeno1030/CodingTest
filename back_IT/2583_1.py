from collections import deque


def bfs(row_i, col_i):
    q = deque()
    q.append((row_i, col_i))
    area = 0
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] != 1:
                matrix[nx][ny] = 1
                area += 1
                q.append((nx, ny))
    return area


if __name__ == "__main__":

    answer = []

    M, N, K = map(int, input().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    rectangles = []
    for _ in range(K):
        a, b, c, d = map(int, input().split())
        rectangles.append((a, b, c, d))

    matrix = [[0] * N for _ in range(M)]

    for x1, y1, x2, y2 in rectangles:
        for i in range(y1, y2):
            for j in range(x1, x2):
                matrix[i][j] = 1

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                result = bfs(i, j)
                if result == 0:
                    answer.append(1)
                else:
                    answer.append(result)

    answer.sort()
    print(len(answer))
    print(*answer)