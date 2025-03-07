def dfs(x, y):
    visited[x][y] = True
    current_color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
            if not visited[nx][ny]:
                if matrix[nx][ny] == current_color:
                    dfs(nx, ny)

if __name__ == '__main__':
    n = int(input())
    matrix = [list(input().rstrip()) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    three_cnt, two_cnt = 0, 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]


    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j)
                three_cnt += 1

    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'R':
                matrix[i][j] = 'G'

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j)
                two_cnt += 1

    print(three_cnt, two_cnt)


