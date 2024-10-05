from collections import deque


def dfs(x):
    visited_d[x] = True
    print(x, end=" ")
    for i in range(1, n + 1):
        if not visited_d[i] and arr[x][i]:
            dfs(i)

def bfs(x):
    q = deque()
    q.append(x)
    visited_b[x] = True
    while q:
        i = q.popleft()
        print(i, end=" ")
        for j in range(1, n + 1):
            if not visited_b[j] and arr[i][j]:
                q.append(j)
                visited_b[j] = True



if __name__ == "__main__":
    n, m, v = map(int, input().split())
    arr = [[False] * (n + 1) for _ in range(n + 1)]
    visited_d = [False] * (n + 1)
    visited_b = [False] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        arr[a][b] = True
        arr[b][a] = True

    dfs(v)
    print()
    bfs(v)