# 게임의 크기는 10 x 10
# 사다리를 이용해 이동한 칸은 기존 칸보다 크고, 뱀 칸은 작다
from collections import deque


def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        x = q.popleft()
        for i in range(1, 7):
            nx = x + i

            if 0 < nx <= 100 and not visited[nx]:
                if nx in ladder.keys():
                    nx = ladder[nx]
                if nx in snake.keys():
                    nx = snake[nx]
                if not visited[nx]:
                    q.append(nx)
                    visited[nx] = True
                    arr[nx] = arr[x] + 1


if __name__ == "__main__":
    arr = [0] * 101
    n, m = map(int, input().split())
    ladder = dict()
    snake = dict()
    visited = [False] * 101
    for _ in range(n):
        start, end = map(int, input().split())
        ladder[start] = end
    for _ in range(m):
        start, end = map(int, input().split())
        snake[start] = end

    bfs(1)
    print(arr[100])