from collections import deque


def bfs():
    q = deque()
    max_day = 0

    # 처음부터 익어있는 토마토의 위치를 큐에 넣음
    for i in range(row):
        for j in range(col):
            if box[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))
                max_day = max(max_day, box[nx][ny] - 1)

    return max_day


if __name__ == "__main__":
    col, row = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(row)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = bfs()

    # 모든 토마토가 익었는지 확인
    if any(0 in row for row in box):
        print(-1)  # 익지 않은 토마토가 있으면 -1 출력
    else:
        print(answer)  # 모든 토마토가 익는데 걸린 일수 출력