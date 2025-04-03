from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True  # 시작점 방문 처리
    count = 1  # 시작점도 포함해야 하므로 1로 초기화

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                q.append((nx, ny))
                count += 1  # 연결된 1의 개수 증가
    return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = []

    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                answer.append(bfs(i, j))

    if len(answer) == 0:
        print(len(answer))
        print(0)
    else:
        print(len(answer))
        print(max(answer))
